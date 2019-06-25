from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from accounts.models import User
from phdfellows.models import Application
from django.utils.translation import ugettext_lazy as _

class ApplicationForm(forms.ModelForm):
    class Meta():
        model = Application
        exclude = ('submitted_at','current_status','previous_status','user','application_no','first_name','last_name','email')

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
            self.fields[field].null = True

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if 'save_as_draft' in self.data:
            return address
        elif 'submit_application' in self.data:
            if (address == ''):
                raise forms.ValidationError(_("Address is required"))
            return address

    def clean_research_area(self):
        research_area = self.cleaned_data.get('research_area')
        if 'save_as_draft' in self.data:
            return research_area
        elif 'submit_application' in self.data:
            if (research_area == ""):
                raise forms.ValidationError(_("Research Area is required"))
            return research_area

    def clean_score_in_ug(self):
        score_in_ug = self.cleaned_data.get('score_in_ug')
        if 'save_as_draft' in self.data:
            return score_in_ug
        elif 'submit_application' in self.data:
            if (score_in_ug == None):
                raise forms.ValidationError(_("Score in UG is required"))
            return score_in_ug

    def clean_applying_for(self):
        applying_for = self.cleaned_data.get('applying_for')
        if 'save_as_draft' in self.data:
            return applying_for
        elif 'submit_application' in self.data:
            if (applying_for == ''):
                raise forms.ValidationError(_("Applying for field is required"))
            return applying_for

    def clean_enrollment_type(self):
        enrollment_type = self.cleaned_data.get('enrollment_type')
        if 'save_as_draft' in self.data:
            return enrollment_type
        elif 'submit_application' in self.data:
            if (enrollment_type == ''):
                raise forms.ValidationError(_("Enrollment Type is required"))
            return enrollment_type

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if 'save_as_draft' in self.data:
            return gender
        elif 'submit_application' in self.data:
            if (gender == ''):
                raise forms.ValidationError(_("Gender is required"))
            return gender

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if 'save_as_draft' in self.data:
            return phone_no
        elif 'submit_application' in self.data:
            if (phone_no == ''):
                raise forms.ValidationError(_("Phone No is required"))
            return phone_no

    def clean_state(self):
        state = self.cleaned_data.get('state')
        if 'save_as_draft' in self.data:
            return state
        elif 'submit_application' in self.data:
            if (state == ''):
                raise forms.ValidationError(_("State is required"))
            return state

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if 'save_as_draft' in self.data:
            return city
        elif 'submit_application' in self.data:
            if (city == ''):
                raise forms.ValidationError(_("City is required"))
            return city

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if 'save_as_draft' in self.data:
            return date_of_birth
        elif 'submit_application' in self.data:
            if (date_of_birth == None):
                raise forms.ValidationError(_("Date of birth is required"))
            return date_of_birth

    def clean_pin_code(self):
        pin_code = self.cleaned_data.get('pin_code')
        if 'save_as_draft' in self.data:
            return pin_code
        elif 'submit_application' in self.data:
            if (pin_code == ''):
                raise forms.ValidationError(_("Pincode is required"))
            return pin_code

    def clean_score_in_ug(self):
        score_in_ug = self.cleaned_data.get('score_in_ug')
        if 'save_as_draft' in self.data:
            return score_in_ug
        elif 'submit_application' in self.data:
            if (score_in_ug == None):
                raise forms.ValidationError(_("Score in UG is required"))
            return score_in_ug

    def clean_scale_of_score_ug(self):
        scale_of_score_ug = self.cleaned_data.get('scale_of_score_ug')
        if 'save_as_draft' in self.data:
            return scale_of_score_ug
        elif 'submit_application' in self.data:
            if (scale_of_score_ug == ''):
                raise forms.ValidationError(_("Scale of Score in UG is required"))
            return scale_of_score_ug

    def clean_ug_discipline(self):
        ug_discipline = self.cleaned_data.get('ug_discipline')
        if 'save_as_draft' in self.data:
            return ug_discipline
        elif 'submit_application' in self.data:
            if (ug_discipline == ''):
                raise forms.ValidationError(_("UG Discipline is required"))
            return ug_discipline

    def clean_ug_college_or_university(self):
        ug_college_or_university = self.cleaned_data.get('ug_college_or_university')
        if 'save_as_draft' in self.data:
            return ug_college_or_university
        elif 'submit_application' in self.data:
            if (ug_college_or_university == ''):
                raise forms.ValidationError(_("UG College/University is required"))
            return ug_college_or_university

    def clean_pg_passed_or_expected_to_pass_in_year(self):
        pg_passed_or_expected_to_pass_in_year = self.cleaned_data.get('pg_passed_or_expected_to_pass_in_year')
        if 'save_as_draft' in self.data:
            return pg_passed_or_expected_to_pass_in_year
        elif 'submit_application' in self.data:
            if (pg_passed_or_expected_to_pass_in_year == ''):
                raise forms.ValidationError(_("PG passed year or expected to pass in year is required"))
            return pg_passed_or_expected_to_pass_in_year

    def clean_score_in_pg(self):
        score_in_pg = self.cleaned_data.get('score_in_pg')
        if 'save_as_draft' in self.data:
            return score_in_pg
        elif 'submit_application' in self.data:
            if (score_in_pg == None):
                raise forms.ValidationError(_("Score in PG is required"))
            return score_in_pg

    def clean_scale_of_score_pg(self):
        scale_of_score_pg = self.cleaned_data.get('scale_of_score_pg')
        if 'save_as_draft' in self.data:
            return scale_of_score_pg
        elif 'submit_application' in self.data:
            if (scale_of_score_pg == ''):
                raise forms.ValidationError(_("Scale of score in PG is required"))
            return scale_of_score_pg

    def clean_pg_discipline(self):
        pg_discipline = self.cleaned_data.get('pg_discipline')
        if 'save_as_draft' in self.data:
            return pg_discipline
        elif 'submit_application' in self.data:
            if (pg_discipline == ''):
                raise forms.ValidationError(_("PG Discipline is required"))
            return pg_discipline

    def clean_pg_college_or_university(self):
        pg_college_or_university = self.cleaned_data.get('pg_college_or_university')
        if 'save_as_draft' in self.data:
            return pg_college_or_university
        elif 'submit_application' in self.data:
            if (pg_college_or_university == ''):
                raise forms.ValidationError(_("PG College/University is required"))
            return pg_college_or_university

    def clean_qualifying_examination(self):
        qualifying_examination = self.cleaned_data.get('qualifying_examination')
        if 'save_as_draft' in self.data:
            return qualifying_examination
        elif 'submit_application' in self.data:
            if (qualifying_examination == ''):
                raise forms.ValidationError(_("Qualifying Examination is required"))
            return qualifying_examination

    def clean_branch_code_for_qualifying_exam(self):
        branch_code_for_qualifying_exam = self.cleaned_data.get('branch_code_for_qualifying_exam')
        if 'save_as_draft' in self.data:
            return branch_code_for_qualifying_exam
        elif 'submit_application' in self.data:
            if (branch_code_for_qualifying_exam == ''):
                raise forms.ValidationError(_("Branch code for qualifying exam is required"))
            return branch_code_for_qualifying_exam

    def clean_qualifying_exam_score_valid_upto(self):
        qualifying_exam_score_valid_upto = self.cleaned_data.get('qualifying_exam_score_valid_upto')
        if 'save_as_draft' in self.data:
            return qualifying_exam_score_valid_upto
        elif 'submit_application' in self.data:
            if (qualifying_exam_score_valid_upto == None):
                raise forms.ValidationError(_("Qualifying exam score valid upto is required"))
            return qualifying_exam_score_valid_upto

    def clean_all_india_rank_in_qualifying_exam(self):
        all_india_rank_in_qualifying_exam = self.cleaned_data.get('all_india_rank_in_qualifying_exam')
        if 'save_as_draft' in self.data:
            return all_india_rank_in_qualifying_exam
        elif 'submit_application' in self.data:
            if (all_india_rank_in_qualifying_exam == None):
                raise forms.ValidationError(_("All India Rank in qualifying exam is required"))
            return all_india_rank_in_qualifying_exam

    def clean_score_in_qualifying_exam(self):
        score_in_qualifying_exam = self.cleaned_data.get('score_in_qualifying_exam')
        if 'save_as_draft' in self.data:
            return score_in_qualifying_exam
        elif 'submit_application' in self.data:
            if (score_in_qualifying_exam == None):
                raise forms.ValidationError(_("Score in qualifying exam is required"))
            return score_in_qualifying_exam

    def clean_work_experience_in_year(self):
        work_experience_in_year = self.cleaned_data.get('work_experience_in_year')
        if 'save_as_draft' in self.data:
            return work_experience_in_year
        elif 'submit_application' in self.data:
            if (work_experience_in_year == ''):
                raise forms.ValidationError(_("Work Experience is required"))
            return work_experience_in_year

    def clean_type_of_work(self):
        type_of_work = self.cleaned_data.get('type_of_work')
        if 'save_as_draft' in self.data:
            return type_of_work
        elif 'submit_application' in self.data:
            if (type_of_work == ''):
                raise forms.ValidationError(_("Type of Work is required"))
            return type_of_work
