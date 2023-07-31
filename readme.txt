 prompt:Create a csv file for three employees for the month of June (30 days), marking the weekend as 0 (Saturday and Sunday), and entering the employee's identification number (EMP001,...)Day, Date (DD-MM-YYYY),Time-in (8:30–10:30), Time-out (5:30–8:30), and Total Hours Worked (Hrs)
 filename:'emp_att_june.csv'

 prompt:Create a CSV file for the month of June that has the following information: Employee ID (EMP001,...), Employee Name, Leave Type (half day, full day), Start Date, End Date, Leave Duration, and Leave Status (Approval Status like Approved or Rejected).
 filename:'emp_leave.csv'

 prompt:Create a csv file for national holidays with the following fields: date (DD-MM-YYYY), day, holiday name, and type (public).
 filename:'emp_holiday.csv'

 prompt:Create a csv file with the following headers: Employee Name, Employee Id (EMP...), Total Working Day (Calculated), and Total Working Hours (Calculated) for three employees for the month of June.depending on the number of working days, with each day's 8 hours of labor, and excluding weekends, holidays, and leaves.
filename:"emp_result_june.csv"




Pseudocode
Set the constant API_KEY to the API key for authentication.
Define  prompts, each having a prompt message and a corresponding filename
Function to generate responses using ChatGPT based on the prompts
Loop through each prompt and generate a response
Prepare the API request options with the prompt, API key, and other parameters.
Send a POST request to the OpenAI API with the options.
Parse the response from the API into JSON format.
Check if the API response contains choices.
If choices exist, retrieve the content of the first choice.
Write the content to a file with the specified filename.
If there is an error writing the file, log the error.
If the file is written successfully, log a success message.
If no choices are found in the API response, log an error message.