<div dir="rtl" align="right">

##### به کمک این ماژول در محیط برنامه‌نویسی پایتون می‌توانید تاریخچه قیمتی حدود ۱۶۰ دارایی در صفحه بازار داخلی سایت tgju را در فرمت پانداز دریافت کنید.

<p>&nbsp;</p>



#### : ازجمله ویژگی‌های مهم این ماژول می‌توان به موارد زیر اشاره کرد
 
قابلیت دسترسی به داده‌های یک نماد موجود در سایت tgju با استفاده از نماد يا نام کامل فارسی  &emsp; <--- &emsp;  <br />
خروجی سازگار با دیتافریم پانداز و قابلیت فیلترینگ زمانی مجدد بر اساس تاریخ شمسی  &emsp; <--- &emsp;  <br />
قابلیت ارائه تاریخ شمسی، میلادی و نام ایام هفته برای داده‌های روزانه  &emsp; <--- &emsp;  <br />
</div>
<p>&nbsp;</p>
<p>&nbsp;</p>

<div dir="rtl" align="right">

# نصب ماژول

</div>

```python
python3 -m pip install tgju_crawl
```


<p>&nbsp;</p>

<div dir="rtl" align="right">

# فراخوانی ماژول


</div>


```python
import tgju_crawl as tg
```

<p>&nbsp;</p>

<div dir="rtl" align="right">

# مشاهده نمادهای موجود در ماژول
<hr style="border:2px solid gray"> </hr>


### : دیتافریم نمادها

</div>

```python
tg.get_df_of_symbols()
```


<div dir="rtl" align="right">

<p>&nbsp;</p>

<div dir="rtl" align="right">

# دریافت تاریخچه قیمت یک نماد
<hr style="border:2px solid gray"> </hr>


### : دریافت تاریخچه قیمتی

</div>

```python
tg.get_tgju_data(symbol = 'انس طلا')
```