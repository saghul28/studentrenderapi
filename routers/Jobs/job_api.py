from typing import Optional, List, Dict
from fastapi import APIRouter, HTTPException
import requests
from bs4 import BeautifulSoup

router = APIRouter()

def scrape_linkedin_jobs(url: str, keyword: str, max_pages: int = 10) -> List[Dict[str, str]]:
    job_details = []

    def linkedin_scraper(webpage, page_number, keyword):
        nonlocal job_details
        next_page = f"{webpage}&start={page_number * 20}"
        response = requests.get(str(next_page))
        
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

        for job_index, job in enumerate(jobs, start=1):
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
            job_location = job.find('span', class_='job-search-card__location').text.strip()
            job_link = job.find('a', class_='base-card__full-link')['href']
            
            # Add job details to list with ID as number
            job_details.append({
                "id": job_index,
                "title": job_title,
                "company": job_company,
                "location": job_location,
                "link": job_link
            })


    for page_number in range(max_pages):
        linkedin_scraper(url, page_number, keyword)
    
    return job_details

@router.get("/jobs/")
def scrape_jobs(location: str, keyword: str, max_pages: Optional[int] = 10):
    url = f'https://www.linkedin.com/jobs/search/?currentJobId=3821979840&geoId=114467055&keywords={keyword}&location={location}&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
    job_details = scrape_linkedin_jobs(url, keyword, max_pages)
    
    if not job_details:
        raise HTTPException(status_code=404, detail="No jobs found")

    return {"jobs": job_details}