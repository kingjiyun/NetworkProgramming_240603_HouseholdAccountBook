#가계부(Household Account Book)
1. startproject householdAccountBook
   1. python -m pip install django~=4.2
   2. django-admin srartproject householdAccountBook .
   3. File > Settings ... ? Language & Frameworks > Django >> [v] Enable Django Support
   4. Run > Edit Configuration...> + Django Server > Name: runserver
   5. VCS > Enable VerSion Control Integation... > git > ok
2. 차트용 실습 : startapp chart_test
 1
3. chart_test/
   1.views
      1. show_chart()
   2. templates
   3. Views
      1. CategarylistView
      2. AccountBookListView
      2. AccountBookCreatView
      3. AccountBookUpdateView
      4. AccountBookDeleteView
   4. templates
      1. categary_list.html
      2. accountbook_apdate.html
      3. accountbook_confirm_delete.html
      4. accountbook_confirm_delete.html
   5. urls
      1. accountbook:categary_list
      2. accountbook:accountbook_list
      3. accountbook:accountbook_create
      3. accountbook:accountbook_update
      4. accountbook:accountbook_delete
      
   