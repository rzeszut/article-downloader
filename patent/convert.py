import models

def convert_inventor(inventor):
    return models.Inventor(inventor = inventor)

def convert_applicant(applicant):
    return models.Applicant(applicant = applicant)

def convert_international_classification(ic):
    return models.InternationalClassification(international_classification = ic)

def convert_cooperative_classification(cc):
    return models.CooperativeClassification(cooperative_classification = cc)

def convert_patent(patent_page):
    inventors = map(convert_inventor, patent_page.inventors)
    applicants = map(convert_applicant, patent_page.applicants)
    international_classifications = map(convert_international_classification,
                                        patent_page.international_classification)
    cooperative_classifications = map(convert_cooperative_classification,
                                      patent_page.cooperative_classification)
    return models.Patent(name = patent_page.name,
                         date = patent_page.date,
                         application_number = patent_page.application_number,
                         priority_number = patent_page.priority_number,
                         abstract = patent_page.abstract,
                         inventors = inventors,
                         applicants = applicants,
                         international_classifications = international_classifications,
                         cooperative_classifications = cooperative_classifications)

