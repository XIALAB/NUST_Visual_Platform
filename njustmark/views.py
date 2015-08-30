# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from django.shortcuts import render,render_to_response
from django.template import Template, Context, RequestContext
from django.http import HttpResponse
import settings
import random
import os
import xlwt
import re

INDEX = 0
RIVIWE_TEXT_LIST = []
DOC_ID = 0
REVIEW_ID = 0
WORKBOOK = xlwt.Workbook(encoding="ascii")
WORKSHEET = WORKBOOK.add_sheet("Sheet",cell_overwrite_ok=True)
COL = 0
ROW = 0

def back(request):
    global ROW
    ROW = ROW -1
    return HttpResponse("回退success")

def download(request):
    global DOWNLOAD_NAME
    wrapper = open(DOWNLOAD_NAME, "rb+").read()
    print wrapper
    print DOWNLOAD_NAME
    print os.path.getsize(DOWNLOAD_NAME)
    response = HttpResponse(wrapper, content_type='application/-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' % DOWNLOAD_NAME
    return response


def nexttext(request):
    global INDEX
    global REVIEW_ID
    ct=RIVIWE_TEXT_LIST[INDEX]
    INDEX+=1
    REVIEW_ID+=1
    print ct
    return HttpResponse(ct)

def save(request):
    global WORKBOOK
    global WORKSHEET
    global COL
    global ROW
    global DOWNLOAD_NAME
    filename = 'temp_savefile-%d.xls' % random.randint(0, 100000)
    WORKBOOK.save(filename)
    if os.path.exists(filename):
        # wrapper = FileWrapper(file(filename))
        #response = HttpResponse(wrapper, content_type='text/plain')
        #print os.path.getsize(filename)
        #response['Content-Encoding'] = 'utf-8'
        #response['Content-Disposition'] = 'attachment;filename=%s' % filename
        DOWNLOAD_NAME = filename
        return HttpResponse(filename)
    else:
        return HttpResponse("保存失败！内存表出错，请重试。")

def ReExce(request):
    print 'reexce'
    global WORKBOOK
    global WORKSHEET
    global COL
    global ROW
    global REVIEW_ID
    global DOC_ID
    if request:
        text = request.POST.get("text")
        mark = request.POST.get("mark")
        txtlist = text.split(",")
        marklist = mark.split(",")
        count = 0
        ROW = ROW +1
        COL = 0
        if text == "":
            HttpResponse("没有任何标记内容，请检查！")
        while count < len(txtlist):
            if marklist[count] == "Feature":
                WORKSHEET.write(ROW, COL+2, txtlist[count])
                count=count+1
                print "Feature"
                continue
            elif marklist[count]=="ADV":
                WORKSHEET.write(ROW, COL+3, txtlist[count])
                count=count+1
                print "ADV"
                continue
            elif marklist[count]=="ADJ":
                WORKSHEET.write(ROW, COL+4, txtlist[count])
                count=count+1
                print "ADJ"
                continue
            elif marklist[count]=="polarity":
                WORKSHEET.write(ROW, COL+5, txtlist[count])
                count=count+1
                print "polarity"
                continue
            elif marklist[count]=="flag":
                WORKSHEET.write(ROW, COL+6, txtlist[count])
                count=count+1
                print "flag"
                continue
            elif marklist[count]=="negation":
                WORKSHEET.write(ROW, COL+7, txtlist[count])
                count=count+1
                print "negation"
                continue
            elif marklist[count]=="contrast":
                WORKSHEET.write(ROW, COL+8, txtlist[count])
                count=count+1
                print "contrast"
                continue
            elif marklist[count]=="transition":
                WORKSHEET.write(ROW, COL+9, txtlist[count])
                count=count+1
                print "transition"
                continue
            elif marklist[count]=="virtual":
                WORKSHEET.write(ROW, COL+10, txtlist[count])
                count=count+1
                print "virtual"
                continue
            elif marklist[count]=="question":
                WORKSHEET.write(ROW, COL+11, txtlist[count])
                count=count+1
                print "ADV"
                continue
            elif marklist[count]=="remarks":
                WORKSHEET.write(ROW, COL+12, txtlist[count])
                count=count+1
                print "remarks"
                break
            else:
                print "fuckoff！"
                count=count+1
        WORKSHEET.write(ROW,COL,DOC_ID)
        WORKSHEET.write(ROW,COL+1,REVIEW_ID)
        return HttpResponse("写入成功!")
    else:
        return HttpResponse("写入失败，非法请求")

def index(request):
    return render(request, "njustmark/index.html")


def upload(request):
    global RIVIWE_TEXT_LIST
    global REVIEW_ID
    global DOC_ID
    global WORKBOOK
    global WORKSHEET
    global COL
    global ROW
    global INDEX
    # get file
    ROW = 0
    file_obj = request.FILES.get('textfile', None)
    RIVIWE_TEXT_LIST = []
    if file_obj == None:
        return HttpResponse('file not existing in the request')
    DOC_ID = str(file_obj)
    file_name = 'temp_file-%d.txt' % random.randint(0, 100000)
    file_full_path = os.path.join(settings.BASE_DIR, file_name)
    dest = open(file_full_path, 'wb+')
    dest.write(file_obj.read())
    dest.close()
    print "文件获取成功"
    # chuli
    file = open(file_full_path)


    p2 = re.compile(r'^<REVIEW_ID>+')
    while 1:
        idline = file.readline()
        matchid = p2.match(idline)
        if matchid:
            break
    idline = idline.replace('<REVIEW_ID>', '')
    idline = idline.replace('</REVIEW_ID>', '')
    REVIEW_ID = idline

    pattern = re.compile(r'^<REVIEW_TEXT>+')
    while 1:
        line = file.readline()
        if not line:
            break
        else:
            match = pattern.match(line)
            if match:
                RIVIWE_TEXT_LIST.append(line)

    for i in range(len(RIVIWE_TEXT_LIST)):
        RIVIWE_TEXT_LIST[i] = RIVIWE_TEXT_LIST[i].replace('<REVIEW_TEXT>', '')
        RIVIWE_TEXT_LIST[i] = RIVIWE_TEXT_LIST[i].replace('</REVIEW_TEXT>', '')
    print "RIVIEW处理完成"
    # chushihua
    WORKSHEET.write(ROW, COL, "doc-id")
    COL += 1
    WORKSHEET.write(ROW, COL, "review-id")
    COL += 1
    WORKSHEET.write(ROW, COL, "Feature")
    COL += 1
    WORKSHEET.write(ROW, COL, "ADV")
    COL += 1
    WORKSHEET.write(ROW, COL, "ADJ")
    COL += 1
    WORKSHEET.write(ROW, COL, "polarity")
    COL += 1
    WORKSHEET.write(ROW, COL, "flag")
    COL += 1
    WORKSHEET.write(ROW, COL, "negation")
    COL += 1
    WORKSHEET.write(ROW, COL, "contrast")
    COL += 1
    WORKSHEET.write(ROW, COL, "transition")
    COL += 1
    WORKSHEET.write(ROW, COL, "virtual")
    COL += 1
    WORKSHEET.write(ROW, COL, "question")
    COL += 1
    WORKSHEET.write(ROW, COL, "remarks")

    print "xls初始化成功"
    t1 = "<h3>" +RIVIWE_TEXT_LIST[0]+"</h3>"
    re_number = len(RIVIWE_TEXT_LIST)
    marked_number = 0
    returnlist = {
        "text": t1,
        "update_success": 1,
        "DOC_ID": DOC_ID,
        "REVIEW_ID": REVIEW_ID,
        "remaining_number":re_number,
        "marked_number":marked_number,

    }
    INDEX = 0
    INDEX += 1
    REVIEW_ID = int(REVIEW_ID)

    return render(request,'njustmark/index.html', returnlist)



