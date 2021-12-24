# **DỰ ĐOÁN KÍCH THƯỚC BÀN CHÂN CỦA KHÁCH HÀNG**

## Nhóm TTP:

1. Nguyễn Thành Trung - 19522432
2. Trần Hồ Thiên Phước - 19522057

## Bài toán dùng ở đâu và để làm gì:
- Bài toán tích hợp trên một app có chức năng chụp/quét và nên thuộc quyền sở hữu bởi 1 shop giày. (Shop giày sản xuất những chiếc giày có giá phổ thông nhằm hướng đến đối tượng khách hàng bình dân)
- Đối tượng sử dụng: những người có nhu cầu mua giày custom size nhưng lại ở qua xa shop, những người bị ảnh hưởng việc đi lại bởi dịch covid. (Đối tượng hướng đến chủ yếu có kinh tế thuộc diện trung bình khá/ các bạn trẻ, học sinh, sinh viên nên giày được đề cập trong đồ án không được sản xuất bằng các chất liệu xịn để có giá thành phổ thông nhất đến với khách hàng (400k vnd < x < 900k vnd)).
- Bài toán nhằm thay thế việc đo đạc thủ công, đảm bảo giày được mua đúng kích thước khách hàng yêu cầu và tăng sự đa dạng size giày của shop, giúp việc mua bán diễn ra nhanh hơn thông qua dữ liệu thu thập được từ những khách hàng đã sử dụng đủ lớn.

## Bài toán gồm:

1. Input: Một tấm ảnh bàn chân.
2. Output: Kết quả là kích thước của bàn chân.

## Mô tả dữ liệu:

- Dự kiến ~1200 ảnh do chính các thành viên chụp.
- Thông số: chiều dài bàn chân (ảnh chụp hướng lòng trong bàn chân: tính từ ngón chân dài nhất đến gót chân), chiều rộng bàn chân (ảnh chụp từ trên xuống và chính diện bàn chân), chiều cao tính từ phần chân chạm đất đến mu bàn chân và mắt cá chân (ảnh chụp hướng vào máng ngoài bàn chân).

Ví dụ:

![image](https://user-images.githubusercontent.com/76487372/147303092-64719c0e-aac5-46f2-9655-7f449044f09d.png)
                            Hình 1. Ảnh chụp hướng lòng trong bàn chân


![image](https://user-images.githubusercontent.com/76487372/147303450-79fb205d-c273-4940-8cb8-95fe589145cd.png)
                            Hình 2. Ảnh chụp từ trên xuống và chính diện bàn chân


![image](https://user-images.githubusercontent.com/76487372/147303462-513ee868-9512-4e7b-aa9e-7fb2c23b453b.png)
                            Hình 3. Chiều cao bàn chân.


- Dữ liệu được chia theo tỉ lệ 70%-train, 15%-dev, 15%-test.

## Mô hình:

- Đánh giá qua độ chính xác, F1-score.
- Mục tiêu dự kiến: Xác định được mô hình tốt nhất, kết quả dự đoán khớp với kích thước bàn chân thực tế, giá trị accuracy và F1-score đều >=0.8 .




