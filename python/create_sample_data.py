import names
import random
import barnum

# code to generate sample data for testing

for i in range(1,10000):
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    loc = barnum.create_city_state_zip()
    zip_code = loc[0]
    city = loc[1]
    state = loc[2]
    phone = barnum.create_phone()
    email = barnum.create_email()
    company = barnum.create_company_name()
    job_title =barnum.create_job_title().replace(',', '-')
    twitter_username = '@'+first_name+'_'+last_name

    with open('sample_data.csv', 'a') as sample_file:

        sample_file.write(email + ',' + first_name + ',' + last_name + ',' + company + ',' + phone + ',' + 'US' + ',' + job_title + ',' + zip_code + ',' + state + ',' + city + ',,' + twitter_username  )
        if i < 9999:
            sample_file.write('\n')
