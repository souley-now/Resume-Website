import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_read_resume(self):

        # Expected output
        expected_output = [
            "John Doe",
            "Courses: CIT591, CIT592, CIT593",
            "Projects",
            "Ice-Cream-Stand: Developed a simulated day to day dessert shopping. Calculated revenue system.",
            "Supermarket: Simulated customer shopping habits.",
            "Water-Tank: Designed a base level gaming. The game consist of two players.",
            "----------",
            "john.doe@example.com"
        ]

        # Test read_resume function
        sample_resume = "sample_resume.txt"
        self.assertEqual(read_resume(sample_resume), expected_output)
    

    def test_detect_name(self):

        # Expected output
        expected_output = "John Doe"

        # test the name function
        lines = ["John Doe "]
        self.assertEqual(detect_the_name(lines), expected_output)

        # Test lowercase name
        expected_output = "Invalid Name"
        lines = ["john doe"]
        self.assertEqual(detect_the_name(lines), expected_output)


    def test_detect_email(self):
        
        # Expected output
        expected_output = "john.doe@example.com"

        # test email function
        lines = ["Courses", "john.doe@example.com"]
        self.assertEqual(detect_the_email(lines), expected_output)
        
        # test email with whitespace
        expected_output = "john.doe@example.com"
        lines = ["Courses", "   john.doe@example.com"]
        self.assertEqual(detect_the_email(lines), expected_output)
        
        # expeted output for wrong emails
        expect_output = ''

        # resume with numbers in email
        lines = ["Courses", "john.2doe@example.com"]
        self.assertEqual(detect_the_email(lines), expect_output)

        # resume with Uppercase after @ in email
        lines = ["Courses", "john.doe@ExAmple.com"]
        self.assertEqual(detect_the_email(lines), expect_output)

        # resume without .com or .edu in email
        lines = ["Courses", "john.doe@example.org"]
        self.assertEqual(detect_the_email(lines), expect_output)


    def test_detect_project(self):

        # Expected output
        expected_output = ["Ice-Cream-Stand.",
                           "Supermarket.",
                           "Water-Tank."]

        # test project function
        lines = ["Projects:", "Ice-Cream-Stand.", "Supermarket.", "Water-Tank."]
        self.assertEqual(detect_the_project(lines), expected_output)

        # Test projects with whitespace at the beginning / ending of lines
        expected_output = ["Ice-Cream-Stand.",
                           "Supermarket.",
                           "Water-Tank."]

        lines = ["Projects:", "   Ice-Cream-Stand.  ", "   Supermarket.", "        Water-Tank.   "]
        self.assertEqual(detect_the_project(lines), expected_output)
        
        # Test projects with blank lines
        expected_output = ["Ice-Cream-Stand.",
                           "Supermarket.",
                           "Water-Tank."]

        lines = ["Projects:", "", "   Ice-Cream-Stand.  ", "   Supermarket.", "        Water-Tank. ", ""]
        self.assertEqual(detect_the_project(lines), expected_output)


    def test_detect_courses(self):

        # Test course function
        expected_output = ["CIT591", "CIT592", "CIT593"]
        lines = ["Courses: CIT591, CIT592, CIT593"]
        self.assertEqual(detect_the_course(lines), expected_output)

        # Test course with white spaces 
        expected_output = ["CIT591", "CIT592", "CIT593"]
        lines = ["  Courses:   CIT591,   CIT592,     CIT593   "]
        self.assertEqual(detect_the_course(lines), expected_output)

        # Test course with weird punctuation 
        expected_output = ["CIT591", "CIT592", "CIT593"]
        lines = ["Courses:@#$!%& CIT591, CIT592, CIT593"]
        self.assertEqual(detect_the_course(lines), expected_output)


if __name__ == '__main__':
    unittest.main()
