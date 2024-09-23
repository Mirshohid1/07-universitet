from django.contrib import admin
from .models import Faculty, Student, Kafedra, Subject, Teacher, Group

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class KafedraInline(admin.TabularInline):
    model = Kafedra
    extra = 1

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1

class GroupInline(admin.TabularInline):
    model = Group
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', )

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [KafedraInline]
    list_display = ('name', 'active', )

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    inlines = [SubjectInline, TeacherInline, GroupInline]
    list_display = ('name', 'faculty', )

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [GroupInline]
    list_display = ('name', )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [GroupInline]
    list_display = ('first_name', 'last_name', )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ('name', 'subject', 'teacher')