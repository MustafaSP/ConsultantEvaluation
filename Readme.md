<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Danman_Deerlendirme_Arac_0"></a>Danışman Değerlendirme Aracı</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Uygulama kullanıclardan yorum alarak veya csv dosyaları üzerinden topladığı verileri etiketleyerek ve anahtar kelimeleri çıkararak danışmanlarının performansının izlenmesini sağlamaktadır.</p>
<h3 class="code-line" data-line-start=4 data-line-end=5 ><a id="Uygulamann_Temel_Teknolojileri_4"></a>Uygulamanın Temel Teknolojileri</h3>
<p class="has-line-data" data-line-start="6" data-line-end="7">Uygulama python 3.10.10 ile bert classification, bert key extraction, flask, faker ve matplotlib kütüphanelerini kullanarak geliştirilmiştir.</p>
<h3 class="code-line" data-line-start=8 data-line-end=9 ><a id="Uygulamann_zellikleri_8"></a>Uygulamanın Özellikleri</h3>
<p class="has-line-data" data-line-start="10" data-line-end="11">Uygulmada kullanıcın etkileşebileceği bir web sayfası bulunmaktadır. Bu web sayfası üzerinden yorumlar toplanabilmektedir.</p>
<p class="has-line-data" data-line-start="12" data-line-end="13">Uygulama yeni gelecek yorum verileri sınıflandırma performansının iyileştirilebilmesi için eğitim scriptine ve eğitilen modellerin kullanılabilmesi için etiketleme scripti içermektedir.</p>
<p class="has-line-data" data-line-start="14" data-line-end="15">Uygulama yeni gelecek yorum verileri sınıflandırma performansının iyileştirilebilmesi için eğitim scriptine ve eğitilen modellerin kullanılabilmesi için etiketleme scripti içermektedir.</p>
<p class="has-line-data" data-line-start="16" data-line-end="17">Uygulama anahtar kelimelerin çıkarılarak odaklanılması gereken alanların tespit edilmesi için key extraction yapan bir script içermektedir.</p>
<p class="has-line-data" data-line-start="18" data-line-end="19">Uygulama toplanan verileri görselleştirmek için matplotlib tabanlı script içerir.</p>
<h2 class="code-line" data-line-start=21 data-line-end=22 ><a id="Kurulum_21"></a>Kurulum</h2>
<p class="has-line-data" data-line-start="23" data-line-end="24">Kullanılan python sürümü 3.10.10</p>
<pre><code class="has-line-data" data-line-start="26" data-line-end="28" class="language-sh">pip install -r requirements.txt
</code></pre>
<h2 class="code-line" data-line-start=29 data-line-end=30 ><a id="altrma_29"></a>Çalıştırma</h2>
<h4 class="code-line" data-line-start=31 data-line-end=32 ><a id="Yorum_sitesini_amak_iin_31"></a>Yorum sitesini açmak için</h4>
<pre><code class="has-line-data" data-line-start="34" data-line-end="37" class="language-sh"><span class="hljs-built_in">cd</span> CommentsGather/Flask
python3 view.py
</code></pre>
<h4 class="code-line" data-line-start=37 data-line-end=38 ><a id="Danman_deerlendirme_37"></a>Danışman değerlendirme</h4>
<pre><code class="has-line-data" data-line-start="40" data-line-end="42" class="language-sh">python3 ConsultantEvaluation.py 
</code></pre>
<blockquote>
<p class="has-line-data" data-line-start="42" data-line-end="43">Not: Hızlı sonuç almak için <a href="http://ConsultantEvaluation.py">ConsultantEvaluation.py</a> içerisine maxRow parametresi koyulmuştur. Dilerseniz düzenleyebilir veya kaldırabilirsiniz</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="44" data-line-end="45">Not: Sonuçlar Outputs altında timestamp damgalı olarak verilmektedir.</p>
</blockquote>
<h2 class="code-line" data-line-start=46 data-line-end=47 ><a id="Baz_Dosya_ve_klasrlerin_levleri_46"></a>Bazı Dosya ve klasörlerin İşlevleri</h2>
<blockquote>
<p class="has-line-data" data-line-start="48" data-line-end="49">NlpProcess/Train.py dosyası etiketleme modeli eğitmektedir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="50" data-line-end="51">NlpProcess/KeyExtractor.py dosyası anahtar kelimeleri çıkarmakta ve yüzdelik dilimlere dönüştürmektedir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="52" data-line-end="53">NlpProcess/SentimentLabeling.py dosyası önceden eğitilmiş model ile yorumların etiketlemesini yapmaktadır.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="54" data-line-end="55">NlpProcess/Preprocces klasörü içerisindeki dosyalar yorumları temizlemekte ve stopwordsleri atmaktadır.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="56" data-line-end="57">NlpProcess/Preprocces klasörü içerisindeki dosyalar bazı değişkenleri tutmaktadır</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="58" data-line-end="59">DataLoader klasörü içerisindeki dosyalar veri tabanından ve csv den verileri okumakta, yorumları temizlemekte ve istenen formata getirmektedir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="60" data-line-end="61">Faker klasörü içerisindeki dosya sahte mail,isim vs. yaratarak test edilebilirliği sağlamaktadır.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="62" data-line-end="63">Graphic klasörü içerisindeki dosya verileri çubuk grafiklere dökmektedir.</p>
</blockquote>
<h2 class="code-line" data-line-start=64 data-line-end=65 ><a id="Gelitirilebilecek_zellikler_64"></a>Geliştirilebilecek Özellikler</h2>
<p class="has-line-data" data-line-start="65" data-line-end="66">Zamanla geliştirilebilecek birkaç konu aşağıda bulunmaktadır.</p>
<blockquote>
<p class="has-line-data" data-line-start="67" data-line-end="68">Zaman kısıtından dolayı Train ederken düşük batch_size ve epochs kullanılarak eğitim yaptım. Daha fazla batch_size ve epochs kullanılarak daha iyi bir model elde edilebilir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="69" data-line-end="70">Metin temizleme geliştirilebilir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="71" data-line-end="72">Daha iyi bir arayüzle yorum alınabilir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="73" data-line-end="74">Daha farklı değerelendirmeler yapılabilir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="75" data-line-end="76">Daha iyi bir arayüzle yorum alınabilir.</p>
</blockquote>
<blockquote>
<p class="has-line-data" data-line-start="77" data-line-end="78">Çok daha iyi bir veri görselleştirmesi yapılabilir.</p>
</blockquote>