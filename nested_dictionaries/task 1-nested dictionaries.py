from job_icy import response


roles = response['jobs']
print(roles)

# def remote_role(roles):

for role in roles:

    """
    Iterates through a list of roles.
    
    Checks if the job title contains the word 'Senior'.

    if it has senior in it then, print actual _job.

    if it doesnt then, it is added to the manager_job.

    """
    
    actual_job = role['jobTitle']
    if 'Senior' in role['jobTitle']:

       print(actual_job)
       
    
    manager_job = role['jobTitle']
    if 'Senior' not  in role['jobTitle']:
       print(manager_job)


     
   
               



