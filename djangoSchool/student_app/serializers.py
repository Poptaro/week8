from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    # fields = '__all__'
    exclude = ['subjects']

class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subject
    fields = '__all__'

class StudentSubjectSerializer(serializers.ModelSerializer):

  subjects = serializers.SerializerMethodField()

  class Meta:
    model = Student
    fields = "__all__"

  def get_subjects(self, instance):
    subjects = instance.subjects.all()
    return SubjectSerializer(subjects, many=True).data