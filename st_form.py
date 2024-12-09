import streamlit as st

st.title('st.form')

# 'with' 표기법을 사용한 전체 예시
st.header('1. `with` 표기법 사용 예시')
st.subheader('SANDWICH')

with st.form('my_form'):
    st.subheader('**샌드위치 주문하기**')

    # 입력 위젯
    coffee_bean_val = st.selectbox('종류', ['참치 샌드위치', '쉬림프 샌드위치','아보카도 샌드위치','로스트 비프 샌드위치'])
    coffee_roast_val = st.selectbox('빵', ['화이트', '하티','파마산오레가노','위트','허니오트','플랫'])
    brewing_val = st.selectbox('치즈', ['아메리칸 치즈', '슈레드 치즈', '모차렐라 치즈'])
    serving_type_val = st.selectbox('소스', ['마요네즈', '스위트 어니언', '칠리','허니 머스타드','홀스레디쉬','스모크 바비큐'])
    milk_val = st.select_slider('빵 굽기', ['없음', '따듯하게', '적당히 굽기', '바삭하게 굽기'])
    owncup_val = st.checkbox('서빙 해주세요')

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        ☕ 주문하신 내용:
        - 종류: `{coffee_bean_val}`
        - 빵: `{coffee_roast_val}`
        - 치즈: `{brewing_val}`
        - 소스: `{serving_type_val}`
        - 빵 굽기: `{milk_val}`
        - 서빙 해주세요: `{owncup_val}`
        ''')
else:
    st.write('☝️ 주문하세요!')


# 객체 표기법을 사용한 짧은 예시
st.header('2. 객체 표기법 예시')

form = st.form('my_form_2')
selected_val = form.slider('값 선택')
form.form_submit_button('제출') #모든 양식은 st.form_submit_button을 포함해야 함.
#st.button과 st.download_button은 양식에 추가할 수 없습니다.
st.write('선택된 값: ', selected_val)
