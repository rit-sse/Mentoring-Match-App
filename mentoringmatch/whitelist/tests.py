from django.test import TestCase
from django.core.exceptions import ValidationError
from whitelist.models import Mentor

class WhiteListSetup(TestCase):
  #make sure that we make the mentor unicode something meaningful
  def test_overridden_mentor_unicode(self):
    mentor = Mentor(dce="deb3323", first_name="Dorrene", last_name="Brown")
    self.assertFalse(str(mentor) == 'Mentor object')

class WhitelistMentorValidation(TestCase):
  def setUp(self):
    self.mentor = Mentor(dce="deb3323", first_name="Dorrene", last_name="Brown")
  
  #------------------ DCE testing ---------------------------------------------
  #make sure proper DCEs go through
  def test_correct_dce(self):
    mentor_dce = "deb3323"
    self.mentor.dce = mentor_dce
    self.assertTrue(self.mentor.dce == mentor_dce)
   
  #throw it garbage as a DCE and make sure it fails
  def test_incorrect_dce(self):
    self.mentor.dce="asd5 3&"
    self.assertRaisesRegexp(ValidationError, "DCE", self.mentor.clean)
    
  #throw it an instructor DCE and make sure it fails  
  def test_nonstudent_dce(self):
    self.mentor.dce="ezcciar"
    self.assertRaisesRegexp(ValidationError, "DCE", self.mentor.clean)
    
  #throw it nothing for the DCE and make sure it fails
  def test_no_dce(self):
    self.mentor.dce=""
    self.assertRaisesRegexp(ValidationError, "DCE", self.mentor.clean)
    
  #throw it a null DCE and make sure it fails 
  def test_null_dce(self):
    self.mentor.dce=None
    self.assertRaisesRegexp(ValidationError, "DCE", self.mentor.clean)
    
  #------------------ First Name testing ---------------------------------------
  #make sure proper names go through
  def test_correct_first_name(self):
    mentor_name = "Dorrene"
    self.mentor.first_name = mentor_name
    self.assertTrue(self.mentor.first_name == mentor_name)
  
  #no names with weird characters
  def test_no_special_chars(self):
    self.mentor.first_name = "This_is_not_a_name!"
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
  
  #make sure names with spaces go through
  def test_correct_first_name_with_spaces(self):
    mentor_name = "Mary Kate"
    self.mentor.first_name = mentor_name
    self.assertTrue(self.mentor.first_name == mentor_name)
    
  #can only have one space, though
  def test_only_one_space_in_first_name(self):
    self.mentor.first_name = "Mary Kate Lastnamebyaccident"
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
   
  #make sure names with dashes go through
  def test_correct_first_name_with_dashes(self):
    mentor_name = "Marie-Claire"
    self.mentor.first_name = mentor_name
    self.assertTrue(self.mentor.first_name == mentor_name)
    
  #can only have one dash, though
  def test_can_only_have_one_dash_in_first_name(self):
    self.mentor.first_name = "Marie-Claire-Etc"
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #throw it whitespace for the first name and make sure it fails
  def test_whitespace_first_name(self):
    self.mentor.first_name=" "
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #throw it nothing for the first name and make sure it fails
  def test_no_first_name(self):
    self.mentor.first_name=""
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #throw it a null first name and make sure it fails
  def test_null_first_name(self):
    self.mentor.first_name=None
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #throw it a first name with numbers and make sure it fails
  def test_first_name_with_numbers(self):
    self.mentor.first_name="deb3323"
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #throw it a first name with characters and make sure it fails
  #throw it whitespace for the first name and make sure it fails
  def test_first_name_with_symbols(self):
    self.mentor.first_name=":)"
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #the first name cannot end in a space  
  def test_first_name_cant_end_with_space(self):
    self.mentor.first_name="Sean "
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
  #the first name cannot end in a dash
  def test_first_name_cant_end_with_dash(self):
    self.mentor.first_name="Sean-"
    self.assertRaisesRegexp(ValidationError, "[F|f]irst [N|n]ame", self.mentor.clean)
    
#------------------Last name testing -------------------------------------------
  #make sure proper last names go through
  def test_correct_last_name(self):
    mentor_name = "Brown"
    self.mentor.last_name = mentor_name
    self.assertTrue(self.mentor.last_name == mentor_name)
  
  #no last names with weird characters
  def test_no_special_chars_in_last_name(self):
    self.mentor.last_name = "This_is_not_a_name!"
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
  
  #no last names with spaces
  def test_no_spaces_in_last_name(self):
    self.mentor.last_name = "Last Name With Spaces"
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
   
  #make sure names with dashes go through
  def test_correct_last_name_with_dashes(self):
    mentor_name = "First-Second"
    self.mentor.last_name = mentor_name
    self.assertTrue(self.mentor.last_name == mentor_name)
    
  #throw it whitespace for the last name and make sure it fails
  def test_whitespace_last_name(self):
    self.mentor.last_name=" "
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
    
  #throw it nothing for the last name and make sure it fails
  def test_no_last_name(self):
    self.mentor.last_name=""
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
    
  #throw it a null last name and make sure it fails
  def test_null_last_name(self):
    self.mentor.last_name=None
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
    
  #throw it a last name with characters and make sure it fails
  def test_last_name_with_symbols(self):
    self.mentor.last_name=":)"
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
    
  #the last name cannot end in a dash
  def test_last_name_cant_end_with_dash(self):
    self.mentor.last_name="Smith-"
    self.assertRaisesRegexp(ValidationError, "[L|l]ast [N|n]ame", self.mentor.clean)
    
  #the last name can end in a period
  def test_correct_last_name_with_period(self):
    mentor_name = "Peterson Jr."
    self.mentor.last_name = mentor_name
    self.assertTrue(self.mentor.last_name == mentor_name)
