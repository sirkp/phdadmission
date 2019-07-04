from django.contrib import admin
from phdfellows.models import Application, WrittenTestScore
# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['application_no', 'first_name', 'last_name', 'date_of_birth', 'gender', 'married',
                'having_disability', 'email', 'phone_no', 'address', 'city', 'pin_code', 'state', 'country',
                'research_area', 'applying_for', 'enrollment_type', 'scale_of_score_ug', 'score_in_ug',
                 'ug_discipline', 'ug_college_or_university', 'pg_passed_or_expected_to_pass_in_year',
                 'scale_of_score_pg', 'score_in_pg', 'pg_discipline', 'pg_college_or_university',
                 'qualifying_examination', 'branch_code_for_qualifying_exam', 'qualifying_exam_score_valid_upto',
                 'all_india_rank_in_qualifying_exam', 'score_in_qualifying_exam', 'work_experience_in_year',
                 'type_of_work', 'no_of_peer_reviewed_publications', 'no_of_patents_granted', 'guide_preference_1',
                 'guide_preference_2', 'guide_preference_3', 'current_status', 'submitted_at', 'submitted_year',
                 'was_selected_for_interview' ]
    list_filter = ['current_status']
    list_display = ['application_no', 'first_name','last_name','email','current_status']

admin.site.register(Application,ApplicationAdmin)
admin.site.register(WrittenTestScore)
