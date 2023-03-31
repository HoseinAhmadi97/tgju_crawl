<div dir="rtl" align="right">

####  به کمک این ماژول می‌توانید تاریخچه قیمت‌های روزانه موجود در سایت اطلاع‌رسانی طلا، سکه و ارز را دریافت کنید که شامل اطلاعات 240 دارایی متفاوت از جمله طلا،   سکه، ارز، حوزه نفت و انرژی، برخی کالاهای جهانی و مهمترین رمز ارزها است که از جمله ویژگی‌های مهم این ماژول می‌توان به موارد زیر اشاره کرد:

امکان دسترسی به تاریخچه قیمت ها در سایت اطلاع رسانی طلا، سکه، ارز &emsp; <--- &emsp;  <br />
خروجی سازگار با دیتافریم پانداز و قابلیت فیلترینگ زمانی مجدد بر اساس تاریخ شمسی  &emsp; <--- &emsp;  <br />
قابلیت ارائه تاریخ شمسی، میلادی و نام ایام هفته برای داده‌های روزانه  &emsp; <--- &emsp;  <br />
</div>

<div dir="rtl" align="left">

# نصب ماژول

</div>

```python
python3 -m pip install tgju_crawl
```


<p>&nbsp;</p>

<div dir="rtl" align="left">

# فراخوانی ماژول


</div>


```python
import tgju_crawl as tg
```

<p>&nbsp;</p>

<div dir="rtl" align="left">

# مشاهده نمادهای موجود در ماژول
<hr style="border:2px solid gray"> </hr>


### : دیتافریم نمادها

</div>

```python
tg.get_df_of_symbols()
```


<div dir="rtl" align="left">

<p>&nbsp;</p>

<div dir="rtl" align="left">

# دریافت تاریخچه قیمت یک نماد
<hr style="border:2px solid gray"> </hr>


### : دریافت تاریخچه قیمتی

</div>

```python

tg.get_tgju_data(symbol = 'حباب نیم سکه')

```