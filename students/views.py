from django.shortcuts import render
from .models import StudentsInfo,GuardianInfo
# , GuardianInfo
# Create your views here.

def GuardianInfoListVW(request):
    all_guardian = GuardianInfo.objects.all()
    context = {"Guardian_list":all_guardian}
    return render(request, 'students/guardian_info_list.html', context)

def GuardianInfoDtlsVW(request, phone_no):
    indiv_guardian = GuardianInfo.objects.get(phone=phone_no)
    context = {"Guardian_Info":indiv_guardian}
    return render(request, 'students/guardian_info_dtls.html',context)

def StudentsInfoListVW(request):
    all_students = StudentsInfo.objects.all()
    context = {"students_list":all_students}
    return render(request, 'students/students_info_list.html', context)

def StudentsInfoDetailsVW(request, student_roll):
    all_students = StudentsInfo.objects.get(roll=student_roll)
    context = {"student_dtls":all_students}
    return render(request, 'students/students_info_dtls.html', context)
