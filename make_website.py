# Souleymane Diallo
# Student ID: 63283765


def read_resume(filename):
    """ 
    - Since the resume file is pretty small, write a function that reads the file and stores it in memory as a list of lines. - Then, you can use list and string manipulations to do all of the other necessary work.
    - You should not prompt the user for a filename (or any other information). You can rely on the provided code which includes hardcoded resume filenames to read.
    """

    # Read resume
    with open(filename, "r") as stream:
        lines = stream.readlines()
    return [line.strip() for line in lines]


def detect_the_name(lines):
    """
    - Detect and return the name by extracting the first line.
    - The one extra thing we want you to do, just for practice, is if the first character in the name string is not uppercase letter (capital 'A' through 'Z'), consider the name  invalid and ignore it. In this case, use 'Invalid Name' as the user's name.
    - For example:
    Brandon Krakowsky is a valid name
    brandon Krakowsky is not a valid name, so your output html file will display 'Invalid Name' instead
    - Another thing to note is that the name on the first line could have leading or trailing
    whitespace, which you will need to remove.
    - Note: Do not use the istitle()function in Python. This returns True if ALL words in a text start with an upper case letter, AND the rest of the characters in each word are lower case letters, otherwise False. This function will incorrectly identify a name like Edward jones as being an invalid name, when it's actually valid.
    """

    # Extract the name 
    name = lines[0].strip()
    if name[0] != name[0].upper():
        return 'Invalid Name'
    return name     
    


def detect_the_email(lines):
    """Detect and return the email address by looking for a line that has the '@' character.
    - For an email to be valid:
        ○ The last four characters of the email need to be either '.com' or '.edu'.
        ○ The email contains a lowercase English character after the '@'.
        ○ There should be no digits or numbers in the email address.
    - These rules will accommodate lbrandon@wharton.upenn.edu but will not accommodate lbrandon@python.org or lbrandon2@wharton.upenn.edu
    - For example:
    lbrandon@wharton.upenn.edu is a valid email
    lbrandon@wharton2.upenn.com is not a valid email
    lbrandon2@wharton.upenn.com is also not a valid email
    - The email string could have leading or trailing whitespace, which will need to be stripped.
    - We are fully aware that these rules are inadequate. However, we want you to use these rules and only these rules.
    - If an email string is invalid based on the given rules, consider the email address to  be missing. This means your function should return an empty string and your output resume file will not display an email address.
    - DO NOT GOOGLE FOR A FUNCTION FOR THIS. Googling for solutions to your homework is an act of academic dishonesty and in this particular case, you will get solutions involving crazy regular expressions, which is a topic we haven't yet discussed in class. (In general, your code should never involve a topic that we have not discussed in class.). Plus, you can easily achieve the required functionality without the use of a regular expression.
    """

    # Loop through the lines of the resume then detect the email with the given constraints
    for line in lines:
        if '@' in line:   # find the email
            email = line.strip() 
            if email.endswith(('.com', '.edu')): # check if the email end with .edu or .com
                if not any(char.isdigit() for char in email): # check for any digits in the email
                    index = email.index('@')
                    if email[index + 1:].islower(): #check for lowercase leters in the email after the '@'
                        return email   
    return '' 


def detect_the_course(lines):
    """
    - Detect and return the courses as a list by looking for the word “Courses” in the  list and then extract the line that contains that word.
    - Then make sure you extract the correct courses. In particular, any random punctuation  after the word “Courses” and before the first actual course needs to be ignored.
    - You are allowed to assume that every course begins with a letter of the English alphabet.
    - Note that the word “Courses”, the random punctuation, or individual courses in the list  could have leading or trailing whitespace that needs removed.
    """
    # Identify the courses
    courses = ""
    for line in lines:
        if 'Courses' in line:
            courses = line.strip()
            break
    
    # Identify courses and remove leading and trailing spaces
    if 'Courses' in courses:
        index = courses.index('Courses') + len('Courses')
        courses = courses[index:].strip()

        # Remove any leading punctuation
        while courses and not courses[0].isalpha():
            courses = courses[1:].strip()

        # Split courses and remove leading/trailing whitespace from each course
        courses_list = [course.strip() for course in courses.split(',')]
        return courses_list
    
    return []


def detect_the_project(lines):
    """
    - Detect and return the projects as a list by looking for the word “Projects” in the  list.
    - Each subsequent line is a project, until you hit a line that contains '----------'. This is NOT an underscore. It is (at least) ten minus signs put together. You have reached the end of the projects section if and only if you see a line that has at least 10 minus signs, one after the other.
    - If you detect a blank line between project descriptions, ignore that line.
    - Each project could have leading or trailing whitespace that needs removed
    """

    projects_section = False
    projects = []

    # Identify the project section and return all the projects
    for line in lines:
        if 'Projects' in line:
            projects_section = True
            continue
        
        # Stop at the dash-line
        if projects_section:    
            if '----------' in line:
                break

            if line.strip(): #ignore blank lines
                projects.append(line.strip())
                
    return projects
        

def read_resume_html_template(template_path):
    """Read HTML resume tamplate file. Return the list of lines from the template."""
    
    with open(template_path, "r") as file:
        lines = file.readlines()
    return lines

def write_resume_html(output_file, content):
    """Write the resume into an HTML formate."""
    
    with open(output_file, 'w') as file:
        file.writelines(content)


def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """
    return "<{}>{}</{}>".format(tag, text, tag)  


def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """
    
    # Create email link in html format
    if '@' in email_address:
        return '<a href="mailto:{}">{}</a>'.format(email_address, email_address.replace("@", "[aT]"))
    return '<a href="mailto:{}">{}</a>'.format(email_address, email_address)



def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """
    # Read and extract html template file
    resume_html_template = "resume_template.html"
    template_lines = read_resume_html_template(resume_html_template)
    
    # Remove the last two lines (</body> and </html>)
    template_lines = template_lines[:-2]
    
    # Read resume file
    lines = read_resume(txt_input_file)

    # Extract information from the resume
    name = detect_the_name(lines)
    email = detect_the_email(lines)
    projects = detect_the_project(lines)
    courses = detect_the_course(lines)
    
    # Generate HTML content
    resume_content = []
    resume_content.append(surround_block('h1', name))
    resume_content.append(surround_block('p', create_email_link(email)))
    resume_content.append(surround_block('h2', 'Projects'))
    resume_content.append(surround_block('ul', ''.join([surround_block('li', project) for project in projects])))
    resume_content.append(surround_block('h2', 'Courses'))
    resume_content.append(surround_block('p', ', '.join(courses)))
    
    # Add the resume content to the template
    final_content = template_lines + ['<div id="page-wrap">'] + resume_content + ['</div>', '</body>', '</html>']
    
    # Write the final HTML to a new file
    write_resume_html(html_output_file, final_content)



def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file


if __name__ == '__main__':
    main()