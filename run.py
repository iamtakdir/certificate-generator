import os
import cv2
import uuid

list_of_names = []



def delete_old_data():
   for i in os.listdir("generated-certificates/"):
      os.remove("generated-certificates/{}".format(i))


def cleanup_data():
   with open('name-data.txt') as f:
      for line in f:
          list_of_names.append(line.strip())


def generate_certificates():

   for index, name in enumerate(list_of_names):
      id = uuid.uuid4()
      certificate_template_image = cv2.imread("certificate-template_python.png")
      cv2.putText(certificate_template_image, name.strip(), (665,781), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (43, 43, 43), 3, cv2.LINE_AA)
      cv2.putText(certificate_template_image, str(id), (551,1206), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (43, 43, 43), 1, cv2.LINE_AA)
      cv2.imwrite("generated-certificates/{}.png".format(id), certificate_template_image)
      print("Processing {} / {}".format(index + 1,len(list_of_names)))
      
def main():
   delete_old_data()
   cleanup_data()
   generate_certificates()



if __name__ == '__main__':
   main()

