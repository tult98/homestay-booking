# Phần Backend của trang web Booking Homestay

## Cấu trúc bao gồm:

	* api
	* homestay
	* homestay2: virtualenv dùng để chạy server
	* json: data để import và database
	* .gitignore
	* EER_Diagram.mwb: cấu trúc database, sử dụng file này để tạo lại bảng trong database
	* EERDiagram.png: ảnh bảng và quan hệ
	* manage.py: quản lý database, chạy lệnh runserver
	* script_insert_db.py: script import database
	* Howtorun.png: ảnh hướng dẫn chạy server

## Để chạy project có thể có 2 cách

	* tạo virtualenv mới python3.7 và install bằng pip theo file requirements.txt đính kèm sau đó nhập python manage.py runserver để chạy 
	* kéo thả trực tiếp file python.exe trong homestay2 vào cmd, sau đó kéo thả manage.py vào cmd + " runserver"
	* địa chỉ truy cập mặc định là: http://localhost:5000 hoặc xem trên cmd
		
## Lưu ý nhỏ là cần tạo database theo yêu cầu thì mới có thể thao tác với database được
	
