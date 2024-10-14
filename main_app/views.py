from django.shortcuts import render
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import time

def index(request):


	# Execute if request if get
	if request.method == "GET":
		return render(request, 'index.html')
	
	# Execute if request is post

	if request.method == "POST":
		file_upload = request.FILES.get('file-upload',None)
		
		if(file_upload == None):
			context = {
			'message': 'لطفا یک فایل با فارمت درست انتخاب بکنید'
    	}
		
			return render(request, 'index.html', context)

		uploaded_image = Image.open(file_upload).resize((250,160))
		
		if uploaded_image.mode in ("RGBA","P"):
			uploaded_image = uploaded_image.convert("RGB")
		timestamp_for_image_name = int(time.time())
		save_path = os.path.join('media/uploads', 'image{0}.jpg'.format(timestamp_for_image_name))

		uploaded_image.save(save_path, format=uploaded_image.format)
		
		original_image_path_open = os.path.join('media/OriginalId','NationalId.jpg')
		

		original_image = Image.open(original_image_path_open).resize((250,160))
		
		if original_image.mode in ("RGBA","P"):
			original_image = original_image.convert("RGB")
			
		original_image.save(original_image_path_open, format=original_image.format)

		original_image = cv2.imread(original_image_path_open)
		uploaded_image = cv2.imread(save_path)


		original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
		uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

		(score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)

		diff = (diff * 255).astype('uint8')

		thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)


		# Draw contours on image

		for c in cnts:
			(x,y,w,h) = cv2.boundingRect(c)
			cv2.rectangle(original_image, (x, y), (x + w, y + h), (0,0,255),2)
			cv2.rectangle(uploaded_image, (x, y), (x + w, y + h),(0,0,255), 2)

		cv2.imwrite(os.path.join('media/GeneratedIds','image_original.jpg'), original_image)
		cv2.imwrite(os.path.join('media/GeneratedIds','image_uploaded.jpg'), uploaded_image)
		cv2.imwrite(os.path.join('media/GeneratedIds', 'image_diff.jpg'), diff)
		cv2.imwrite(os.path.join('media/GeneratedIds','image_thresh.jpg'), thresh)

		context = {
        	'score': str(round(score*100,2)) + '%' + ' correct',
			'message': 'با موفقیت بررسی شد'
    	}
		


		return render(request, 'index.html', context)
	

