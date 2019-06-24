#main.py

from google.cloud import vision
def hello_gcs(event, context):
    file = event

   try:	
    	uri='gs://'+file["bucket"]+"/"+ file["name"]
    	print(uri)
    
    	client = vision.ImageAnnotatorClient()
    	image = vision.types.Image()
    	image.source.image_uri = uri
    
    	objects = client.object_localization(
        image=image).localized_object_annotations
    
    	print('Number of objects found: {}'.format(len(objects)))
    	for object_ in objects:
        	print('\n{} (confidence: {})'.format(object_.name, object_.score))
        	print('Normalized bounding polygon vertices: ')
        	for vertex in object_.bounding_poly.normalized_vertices:
       		     print(' - ({}, {})'.format(vertex.x, vertex.y))
	
   except Exception as e
	raise e

#in requirements.txt
google-cloud-vision
google-cloud-storage
