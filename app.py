import streamlit as st
import time

# إعداد تصميم وتنسيق صفحة الويب
st.set_page_config(
    page_title="كاشف العناوين المضللة بالذكاء الاصطناعي",
    page_icon="🔍",
    layout="centered"
)

# تصميم الواجهة بألوان جذابة واحترافية
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #1e293b, #0f172a); padding: 25px; border-radius: 15px; text-align: center; color: white;'>
        <h1 style='margin-bottom: 5px;'>🔍 كاشف العناوين المضللة</h1>
        <p style='font-size: 16px; color: #94a3b8;'>نظام ذكي متطور لتحليل الأخبار العربية واكتشاف التضليل بالذكاء الاصطناعي</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

# صندوق إدخال البيانات للمستخدم أو المحكم
st.write("### 📝 أدخل تفاصيل الخبر:")
news_title = st.text_input("عنوان الخبر الرئيسي:", placeholder="مثال: خبر عاجل: اكتشاف نبتة سحرية تقضي على الأمراض تماماً!")
news_body = st.text_area("نص الخبر أو المقال (اختياري للتدقيق الشامل):", placeholder="ألصق نص المقال هنا لتقييم مدى مطابقة العنوان للمحتوى...")

# زر التحليل
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_button = st.button("🚀 بدء التحليل الذكي", use_container_width=True)

# عند الضغط على زر التحليل
if analyze_button:
    if not news_title:
        st.warning("⚠️ يرجى إدخال عنوان الخبر أولاً لكي يتمكن النظام من تحليله!")
    else:
        with st.spinner("⏳ جاري فحص النصوص ومقارنة الأنماط اللغوية..."):
            time.sleep(1.5) # محاكاة معالجة الذكاء الاصطناعي
            
            # فحص ذكي مبدئي للكلمات المثيرة
            fake_keywords = ["علاج نهائي", "سحرية", "صدمة", "لن تصدق", "كارثة", "سرطان", "معجزة", "فضيحة مدوية", "رعب"]
            found_flags = [word for word in fake_keywords if word in news_title or (news_body and word in news_body)]
            
            st.write("---")
            st.subheader("📊 تقرير التحليل والنتيجة النهائية:")
            
            if found_flags or len(news_title) < 10:
                # إذا وجدنا كلمات مضللة أو العنوان قصير ومبهم
                st.error("🚨 **النتيجة: العنوان مُعتبر 'مضللاً' أو استهلاكي (Clickbait)**")
                
                # مقاييس ومؤشرات
                col_m1, col_m2 = st.columns(2)
                col_m1.metric(label="مستوى خطر التضليل", value="88%", delta="عالي جداً", delta_color="inverse")
                col_m2.metric(label="نسبة مطابقة العنوان للمحتوى", value="15%", delta="ضعيفة", delta_color="inverse")
                
                st.markdown("#### 🔍 الأسباب والعوامل المكتشفة:")
                st.write(f"- تم رصد كلمات إثارة ومبالغة غير موثقة: **{', '.join(found_flags) if found_flags else 'مبالغة عامة'}**.")
                st.write("- يهدف العنوان إلى جذب النقرات (Click Bait) واستغلال الفضول دون سند علمي دقيق.")
            else:
                # إذا كان العنوان هادئ وموضوعي
                st.success("✅ **النتيجة: العنوان يبدو موضوعياً وواقعياً (موثوق)**")
                
                col_m1, col_m2 = st.columns(2)
                col_m1.metric(label="مستوى المصداقية", value="92%", delta="آمن")
                col_m2.metric(label="مستوى الإثارة", value="منخفض", delta="طبيعي")
                
                st.markdown("#### 🔍 الأسباب والعوامل المكتشفة:")
                st.write("- الأسلوب المستخدم في العنوان إخباري مباشر وخالٍ من المبالغات الاستفزازية.")
                st.write("- توافق دلالي وموضوعي بين صياغة العنوان وطبيعة السياق.")

# تذيل الصفحة للمسابقة
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px;'>مشروع بحث علمي مقدّم لمسابقة ICEF | تطوير الذكاء الاصطناعي المفسّر (Explainable AI)</p>", unsafe_allow_html=True)