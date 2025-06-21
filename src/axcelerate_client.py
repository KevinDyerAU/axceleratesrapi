from typing import Dict, Any, List, Optional
import requests
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class AxcelerateConfig:
    web_service_token: str
    api_token: str
    base_url: str = "https://app.axcelerate.com/api"

class AxcelerateClient:
    def __init__(self, config: AxcelerateConfig):
        self.config = config
        self.headers = {
            'X-WS-TOKEN': config.web_service_token,
            'X-API-TOKEN': config.api_token,
            'Content-Type': 'application/json'
        }

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None) -> Dict:
        """Make a request to the Axcelerate API."""
        url = f"{self.config.base_url}/{endpoint}"
        response = requests.request(
            method,
            url,
            headers=self.headers,
            params=params,
            json=json_data
        )
        response.raise_for_status()
        return response.json()

    def search_contacts(self, search_term: str, display_length: int = 10) -> List[Dict]:
        """Search for contacts in Axcelerate."""
        params = {
            'q': search_term,
            'displayLength': display_length
        }
        return self._make_request('GET', 'contacts/search', params=params)

    def get_course_enrolments(self, contact_id: int) -> List[Dict]:
        """Get all course enrolments for a student."""
        return self._make_request('GET', f'contact/enrolments/{contact_id}')

    def update_assessment(self, enrolment_id: int, outcome_code: str, status: str, comments: Optional[str] = None) -> Dict:
        """Update an assessment for a course enrolment."""
        data = {
            'OUTCOMECODE': outcome_code,
            'STATUS': status,
            'COMMENTS': comments
        }
        return self._make_request('PUT', f'course/enrolment/{enrolment_id}', json_data=data)

    def get_assessment_status(self, enrolment_id: int) -> Dict:
        """Get the current assessment status for a course enrolment."""
        return self._make_request('GET', f'course/enrolment/{enrolment_id}')
