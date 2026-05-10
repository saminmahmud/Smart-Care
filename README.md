
```
Smart Care
├─ .python-version
├─ accounts
│  ├─ admin.py
│  ├─ apps.py
│  ├─ decorators.py
│  ├─ forms.py
│  ├─ managers.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_remove_user_username.py
│  │  ├─ 0003_remove_user_profile_picture.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ appointments
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_appointment_end_time_appointment_start_time_and_more.py
│  │  ├─ 0003_alter_appointment_end_time_and_more.py
│  │  ├─ 0004_prescription_is_active.py
│  │  ├─ 0005_medication_is_active.py
│  │  ├─ 0006_medication_frequency.py
│  │  ├─ 0007_alter_prescription_appointment.py
│  │  ├─ 0008_platformfee.py
│  │  ├─ 0009_payment_stripe_session_id.py
│  │  ├─ 0010_alter_appointment_status.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ build_files.sh
├─ doctors
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_alter_review_patient.py
│  │  ├─ 0003_doctor_is_available.py
│  │  ├─ 0004_alter_doctorschedule_day_of_week.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ utils.py
│  ├─ views.py
│  └─ __init__.py
├─ manage.py
├─ media
│  └─ medical_reports
│     └─ download.jpg
├─ patients
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_patient_height_patient_weight.py
│  │  ├─ 0003_medicalhistory_is_active.py
│  │  ├─ 0004_alter_medicalhistory_is_active.py
│  │  ├─ 0005_familymedicalhistory.py
│  │  ├─ 0006_alter_familymedicalhistory_relation_allergy.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ smart_care
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ staticfiles
│  ├─ admin
│  │  ├─ css
│  │  │  ├─ autocomplete.css
│  │  │  ├─ autocomplete.css.gz
│  │  │  ├─ autocomplete.d24f10bdee41.css
│  │  │  ├─ autocomplete.d24f10bdee41.css.gz
│  │  │  ├─ base.428a30193bdc.css
│  │  │  ├─ base.428a30193bdc.css.gz
│  │  │  ├─ base.css
│  │  │  ├─ base.css.gz
│  │  │  ├─ changelists.css
│  │  │  ├─ changelists.css.gz
│  │  │  ├─ changelists.dc127cbae4a6.css
│  │  │  ├─ changelists.dc127cbae4a6.css.gz
│  │  │  ├─ dark_mode.a364bd93cdcc.css
│  │  │  ├─ dark_mode.a364bd93cdcc.css.gz
│  │  │  ├─ dark_mode.css
│  │  │  ├─ dark_mode.css.gz
│  │  │  ├─ dashboard.css
│  │  │  ├─ dashboard.css.gz
│  │  │  ├─ dashboard.e90f2068217b.css
│  │  │  ├─ dashboard.e90f2068217b.css.gz
│  │  │  ├─ forms.css
│  │  │  ├─ forms.css.gz
│  │  │  ├─ forms.ed9e8bcc72ea.css
│  │  │  ├─ forms.ed9e8bcc72ea.css.gz
│  │  │  ├─ login.a3b47c458e5d.css
│  │  │  ├─ login.a3b47c458e5d.css.gz
│  │  │  ├─ login.css
│  │  │  ├─ login.css.gz
│  │  │  ├─ nav_sidebar.css
│  │  │  ├─ nav_sidebar.css.gz
│  │  │  ├─ nav_sidebar.dd925738f4cc.css
│  │  │  ├─ nav_sidebar.dd925738f4cc.css.gz
│  │  │  ├─ responsive.css
│  │  │  ├─ responsive.css.gz
│  │  │  ├─ responsive.ea11f463f024.css
│  │  │  ├─ responsive.ea11f463f024.css.gz
│  │  │  ├─ responsive_rtl.2429bcdc43db.css
│  │  │  ├─ responsive_rtl.2429bcdc43db.css.gz
│  │  │  ├─ responsive_rtl.css
│  │  │  ├─ responsive_rtl.css.gz
│  │  │  ├─ rtl.5958ec60a803.css
│  │  │  ├─ rtl.5958ec60a803.css.gz
│  │  │  ├─ rtl.css
│  │  │  ├─ rtl.css.gz
│  │  │  ├─ unusable_password_field.b433f2a95fba.css
│  │  │  ├─ unusable_password_field.b433f2a95fba.css.gz
│  │  │  ├─ unusable_password_field.css
│  │  │  ├─ unusable_password_field.css.gz
│  │  │  ├─ vendor
│  │  │  │  └─ select2
│  │  │  │     ├─ LICENSE-SELECT2.f94142512c91.md
│  │  │  │     ├─ LICENSE-SELECT2.f94142512c91.md.gz
│  │  │  │     ├─ LICENSE-SELECT2.md
│  │  │  │     ├─ LICENSE-SELECT2.md.gz
│  │  │  │     ├─ select2.a2194c262648.css
│  │  │  │     ├─ select2.a2194c262648.css.gz
│  │  │  │     ├─ select2.css
│  │  │  │     ├─ select2.css.gz
│  │  │  │     ├─ select2.min.9f54e6414f87.css
│  │  │  │     ├─ select2.min.9f54e6414f87.css.gz
│  │  │  │     ├─ select2.min.css
│  │  │  │     └─ select2.min.css.gz
│  │  │  ├─ widgets.2bfb0f4bb90a.css
│  │  │  ├─ widgets.2bfb0f4bb90a.css.gz
│  │  │  ├─ widgets.css
│  │  │  └─ widgets.css.gz
│  │  ├─ img
│  │  │  ├─ calendar-icons.11b535e4a489.svg
│  │  │  ├─ calendar-icons.11b535e4a489.svg.gz
│  │  │  ├─ calendar-icons.svg
│  │  │  ├─ calendar-icons.svg.gz
│  │  │  ├─ icon-addlink.cf2357b7d0e6.svg
│  │  │  ├─ icon-addlink.cf2357b7d0e6.svg.gz
│  │  │  ├─ icon-addlink.svg
│  │  │  ├─ icon-addlink.svg.gz
│  │  │  ├─ icon-alert-dark.0feae5205d73.svg
│  │  │  ├─ icon-alert-dark.0feae5205d73.svg.gz
│  │  │  ├─ icon-alert-dark.svg
│  │  │  ├─ icon-alert-dark.svg.gz
│  │  │  ├─ icon-alert.22a12b18ffea.svg
│  │  │  ├─ icon-alert.22a12b18ffea.svg.gz
│  │  │  ├─ icon-alert.svg
│  │  │  ├─ icon-alert.svg.gz
│  │  │  ├─ icon-calendar.5ecf61f31b5d.svg
│  │  │  ├─ icon-calendar.5ecf61f31b5d.svg.gz
│  │  │  ├─ icon-calendar.svg
│  │  │  ├─ icon-calendar.svg.gz
│  │  │  ├─ icon-changelink.b592a93b41be.svg
│  │  │  ├─ icon-changelink.b592a93b41be.svg.gz
│  │  │  ├─ icon-changelink.svg
│  │  │  ├─ icon-changelink.svg.gz
│  │  │  ├─ icon-clock.e8021c090c7a.svg
│  │  │  ├─ icon-clock.e8021c090c7a.svg.gz
│  │  │  ├─ icon-clock.svg
│  │  │  ├─ icon-clock.svg.gz
│  │  │  ├─ icon-debug-dark.54c8a9312862.svg
│  │  │  ├─ icon-debug-dark.54c8a9312862.svg.gz
│  │  │  ├─ icon-debug-dark.svg
│  │  │  ├─ icon-debug-dark.svg.gz
│  │  │  ├─ icon-debug.55d305d70611.svg
│  │  │  ├─ icon-debug.55d305d70611.svg.gz
│  │  │  ├─ icon-debug.svg
│  │  │  ├─ icon-debug.svg.gz
│  │  │  ├─ icon-deletelink.d730f4e28cce.svg
│  │  │  ├─ icon-deletelink.d730f4e28cce.svg.gz
│  │  │  ├─ icon-deletelink.svg
│  │  │  ├─ icon-deletelink.svg.gz
│  │  │  ├─ icon-hidelink.e152bbd56430.svg
│  │  │  ├─ icon-hidelink.e152bbd56430.svg.gz
│  │  │  ├─ icon-hidelink.svg
│  │  │  ├─ icon-hidelink.svg.gz
│  │  │  ├─ icon-info-dark.d45fe10cd8bd.svg
│  │  │  ├─ icon-info-dark.d45fe10cd8bd.svg.gz
│  │  │  ├─ icon-info-dark.svg
│  │  │  ├─ icon-info-dark.svg.gz
│  │  │  ├─ icon-info.8d7f595627bc.svg
│  │  │  ├─ icon-info.8d7f595627bc.svg.gz
│  │  │  ├─ icon-info.svg
│  │  │  ├─ icon-info.svg.gz
│  │  │  ├─ icon-no-dark.b8cdf102c9f0.svg
│  │  │  ├─ icon-no-dark.b8cdf102c9f0.svg.gz
│  │  │  ├─ icon-no-dark.svg
│  │  │  ├─ icon-no-dark.svg.gz
│  │  │  ├─ icon-no.030751157345.svg
│  │  │  ├─ icon-no.030751157345.svg.gz
│  │  │  ├─ icon-no.svg
│  │  │  ├─ icon-no.svg.gz
│  │  │  ├─ icon-unknown-alt.36166323e511.svg
│  │  │  ├─ icon-unknown-alt.36166323e511.svg.gz
│  │  │  ├─ icon-unknown-alt.svg
│  │  │  ├─ icon-unknown-alt.svg.gz
│  │  │  ├─ icon-unknown.a3f339db02b7.svg
│  │  │  ├─ icon-unknown.a3f339db02b7.svg.gz
│  │  │  ├─ icon-unknown.svg
│  │  │  ├─ icon-unknown.svg.gz
│  │  │  ├─ icon-viewlink.4a14a61a9e85.svg
│  │  │  ├─ icon-viewlink.4a14a61a9e85.svg.gz
│  │  │  ├─ icon-viewlink.svg
│  │  │  ├─ icon-viewlink.svg.gz
│  │  │  ├─ icon-yes-dark.89c587634cdd.svg
│  │  │  ├─ icon-yes-dark.89c587634cdd.svg.gz
│  │  │  ├─ icon-yes-dark.svg
│  │  │  ├─ icon-yes-dark.svg.gz
│  │  │  ├─ icon-yes.29488ce3e9f8.svg
│  │  │  ├─ icon-yes.29488ce3e9f8.svg.gz
│  │  │  ├─ icon-yes.svg
│  │  │  ├─ icon-yes.svg.gz
│  │  │  ├─ inline-delete.f07da9f66580.svg
│  │  │  ├─ inline-delete.f07da9f66580.svg.gz
│  │  │  ├─ inline-delete.svg
│  │  │  ├─ inline-delete.svg.gz
│  │  │  ├─ README.2e7bc30d034a.md
│  │  │  ├─ README.2e7bc30d034a.md.gz
│  │  │  ├─ README.md
│  │  │  ├─ README.md.gz
│  │  │  ├─ search.b529c8b3d9fb.svg
│  │  │  ├─ search.b529c8b3d9fb.svg.gz
│  │  │  ├─ search.svg
│  │  │  ├─ search.svg.gz
│  │  │  ├─ selector-icons.0c131af266f6.svg
│  │  │  ├─ selector-icons.0c131af266f6.svg.gz
│  │  │  ├─ selector-icons.svg
│  │  │  ├─ selector-icons.svg.gz
│  │  │  ├─ sorting-icons.c9d975052c55.svg
│  │  │  ├─ sorting-icons.c9d975052c55.svg.gz
│  │  │  ├─ sorting-icons.svg
│  │  │  ├─ sorting-icons.svg.gz
│  │  │  ├─ tooltag-add.16a3e1048c7e.svg
│  │  │  ├─ tooltag-add.16a3e1048c7e.svg.gz
│  │  │  ├─ tooltag-add.svg
│  │  │  ├─ tooltag-add.svg.gz
│  │  │  ├─ tooltag-arrowright.838d69f08fa9.svg
│  │  │  ├─ tooltag-arrowright.838d69f08fa9.svg.gz
│  │  │  ├─ tooltag-arrowright.svg
│  │  │  └─ tooltag-arrowright.svg.gz
│  │  └─ js
│  │     ├─ actions.f1d5653edb59.js
│  │     ├─ actions.f1d5653edb59.js.gz
│  │     ├─ actions.js
│  │     ├─ actions.js.gz
│  │     ├─ admin
│  │     │  ├─ DateTimeShortcuts.5a6d4ad12024.js
│  │     │  ├─ DateTimeShortcuts.5a6d4ad12024.js.gz
│  │     │  ├─ DateTimeShortcuts.js
│  │     │  ├─ DateTimeShortcuts.js.gz
│  │     │  ├─ RelatedObjectLookups.ed6240809a40.js
│  │     │  ├─ RelatedObjectLookups.ed6240809a40.js.gz
│  │     │  ├─ RelatedObjectLookups.js
│  │     │  └─ RelatedObjectLookups.js.gz
│  │     ├─ autocomplete.01591ab27be7.js
│  │     ├─ autocomplete.01591ab27be7.js.gz
│  │     ├─ autocomplete.js
│  │     ├─ autocomplete.js.gz
│  │     ├─ calendar.1ba287b592e8.js
│  │     ├─ calendar.1ba287b592e8.js.gz
│  │     ├─ calendar.js
│  │     ├─ calendar.js.gz
│  │     ├─ cancel.ecc4c5ca7b32.js
│  │     ├─ cancel.ecc4c5ca7b32.js.gz
│  │     ├─ cancel.js
│  │     ├─ cancel.js.gz
│  │     ├─ change_form.9d8ca4f96b75.js
│  │     ├─ change_form.9d8ca4f96b75.js.gz
│  │     ├─ change_form.js
│  │     ├─ change_form.js.gz
│  │     ├─ core.7e257fdf56dc.js
│  │     ├─ core.7e257fdf56dc.js.gz
│  │     ├─ core.js
│  │     ├─ core.js.gz
│  │     ├─ filters.0e360b7a9f80.js
│  │     ├─ filters.0e360b7a9f80.js.gz
│  │     ├─ filters.js
│  │     ├─ filters.js.gz
│  │     ├─ inlines.89b3c627c5dc.js
│  │     ├─ inlines.89b3c627c5dc.js.gz
│  │     ├─ inlines.js
│  │     ├─ inlines.js.gz
│  │     ├─ jquery.init.b7781a0897fc.js
│  │     ├─ jquery.init.b7781a0897fc.js.gz
│  │     ├─ jquery.init.js
│  │     ├─ jquery.init.js.gz
│  │     ├─ nav_sidebar.3b9190d420b1.js
│  │     ├─ nav_sidebar.3b9190d420b1.js.gz
│  │     ├─ nav_sidebar.js
│  │     ├─ nav_sidebar.js.gz
│  │     ├─ popup_response.96190d343c22.js
│  │     ├─ popup_response.96190d343c22.js.gz
│  │     ├─ popup_response.js
│  │     ├─ popup_response.js.gz
│  │     ├─ prepopulate.bd2361dfd64d.js
│  │     ├─ prepopulate.bd2361dfd64d.js.gz
│  │     ├─ prepopulate.js
│  │     ├─ prepopulate.js.gz
│  │     ├─ prepopulate_init.6cac7f3105b8.js
│  │     ├─ prepopulate_init.6cac7f3105b8.js.gz
│  │     ├─ prepopulate_init.js
│  │     ├─ prepopulate_init.js.gz
│  │     ├─ SelectBox.7d3ce5a98007.js
│  │     ├─ SelectBox.7d3ce5a98007.js.gz
│  │     ├─ SelectBox.js
│  │     ├─ SelectBox.js.gz
│  │     ├─ SelectFilter2.6f887636b8dc.js
│  │     ├─ SelectFilter2.6f887636b8dc.js.gz
│  │     ├─ SelectFilter2.js
│  │     ├─ SelectFilter2.js.gz
│  │     ├─ theme.91cf832f559e.js
│  │     ├─ theme.91cf832f559e.js.gz
│  │     ├─ theme.js
│  │     ├─ theme.js.gz
│  │     ├─ urlify.ae970a820212.js
│  │     ├─ urlify.ae970a820212.js.gz
│  │     ├─ urlify.js
│  │     ├─ urlify.js.gz
│  │     └─ vendor
│  │        ├─ jquery
│  │        │  ├─ jquery.12e87d2f3a4c.js
│  │        │  ├─ jquery.12e87d2f3a4c.js.gz
│  │        │  ├─ jquery.js
│  │        │  ├─ jquery.js.gz
│  │        │  ├─ jquery.min.2c872dbe60f4.js
│  │        │  ├─ jquery.min.2c872dbe60f4.js.gz
│  │        │  ├─ jquery.min.js
│  │        │  ├─ jquery.min.js.gz
│  │        │  ├─ LICENSE.de877aa6d744.txt
│  │        │  ├─ LICENSE.de877aa6d744.txt.gz
│  │        │  ├─ LICENSE.txt
│  │        │  └─ LICENSE.txt.gz
│  │        ├─ select2
│  │        │  ├─ i18n
│  │        │  │  ├─ af.4f6fcd73488c.js
│  │        │  │  ├─ af.4f6fcd73488c.js.gz
│  │        │  │  ├─ af.js
│  │        │  │  ├─ af.js.gz
│  │        │  │  ├─ ar.65aa8e36bf5d.js
│  │        │  │  ├─ ar.65aa8e36bf5d.js.gz
│  │        │  │  ├─ ar.js
│  │        │  │  ├─ ar.js.gz
│  │        │  │  ├─ az.270c257daf81.js
│  │        │  │  ├─ az.270c257daf81.js.gz
│  │        │  │  ├─ az.js
│  │        │  │  ├─ az.js.gz
│  │        │  │  ├─ bg.39b8be30d4f0.js
│  │        │  │  ├─ bg.39b8be30d4f0.js.gz
│  │        │  │  ├─ bg.js
│  │        │  │  ├─ bg.js.gz
│  │        │  │  ├─ bn.6d42b4dd5665.js
│  │        │  │  ├─ bn.6d42b4dd5665.js.gz
│  │        │  │  ├─ bn.js
│  │        │  │  ├─ bn.js.gz
│  │        │  │  ├─ bs.91624382358e.js
│  │        │  │  ├─ bs.91624382358e.js.gz
│  │        │  │  ├─ bs.js
│  │        │  │  ├─ bs.js.gz
│  │        │  │  ├─ ca.a166b745933a.js
│  │        │  │  ├─ ca.a166b745933a.js.gz
│  │        │  │  ├─ ca.js
│  │        │  │  ├─ ca.js.gz
│  │        │  │  ├─ cs.4f43e8e7d33a.js
│  │        │  │  ├─ cs.4f43e8e7d33a.js.gz
│  │        │  │  ├─ cs.js
│  │        │  │  ├─ cs.js.gz
│  │        │  │  ├─ da.766346afe4dd.js
│  │        │  │  ├─ da.766346afe4dd.js.gz
│  │        │  │  ├─ da.js
│  │        │  │  ├─ da.js.gz
│  │        │  │  ├─ de.8a1c222b0204.js
│  │        │  │  ├─ de.8a1c222b0204.js.gz
│  │        │  │  ├─ de.js
│  │        │  │  ├─ de.js.gz
│  │        │  │  ├─ dsb.56372c92d2f1.js
│  │        │  │  ├─ dsb.56372c92d2f1.js.gz
│  │        │  │  ├─ dsb.js
│  │        │  │  ├─ dsb.js.gz
│  │        │  │  ├─ el.27097f071856.js
│  │        │  │  ├─ el.27097f071856.js.gz
│  │        │  │  ├─ el.js
│  │        │  │  ├─ el.js.gz
│  │        │  │  ├─ en.cf932ba09a98.js
│  │        │  │  ├─ en.cf932ba09a98.js.gz
│  │        │  │  ├─ en.js
│  │        │  │  ├─ en.js.gz
│  │        │  │  ├─ es.66dbc2652fb1.js
│  │        │  │  ├─ es.66dbc2652fb1.js.gz
│  │        │  │  ├─ es.js
│  │        │  │  ├─ es.js.gz
│  │        │  │  ├─ et.2b96fd98289d.js
│  │        │  │  ├─ et.2b96fd98289d.js.gz
│  │        │  │  ├─ et.js
│  │        │  │  ├─ et.js.gz
│  │        │  │  ├─ eu.adfe5c97b72c.js
│  │        │  │  ├─ eu.adfe5c97b72c.js.gz
│  │        │  │  ├─ eu.js
│  │        │  │  ├─ eu.js.gz
│  │        │  │  ├─ fa.3b5bd1961cfd.js
│  │        │  │  ├─ fa.3b5bd1961cfd.js.gz
│  │        │  │  ├─ fa.js
│  │        │  │  ├─ fa.js.gz
│  │        │  │  ├─ fi.614ec42aa9ba.js
│  │        │  │  ├─ fi.614ec42aa9ba.js.gz
│  │        │  │  ├─ fi.js
│  │        │  │  ├─ fi.js.gz
│  │        │  │  ├─ fr.05e0542fcfe6.js
│  │        │  │  ├─ fr.05e0542fcfe6.js.gz
│  │        │  │  ├─ fr.js
│  │        │  │  ├─ fr.js.gz
│  │        │  │  ├─ gl.d99b1fedaa86.js
│  │        │  │  ├─ gl.d99b1fedaa86.js.gz
│  │        │  │  ├─ gl.js
│  │        │  │  ├─ gl.js.gz
│  │        │  │  ├─ he.e420ff6cd3ed.js
│  │        │  │  ├─ he.e420ff6cd3ed.js.gz
│  │        │  │  ├─ he.js
│  │        │  │  ├─ he.js.gz
│  │        │  │  ├─ hi.70640d41628f.js
│  │        │  │  ├─ hi.70640d41628f.js.gz
│  │        │  │  ├─ hi.js
│  │        │  │  ├─ hi.js.gz
│  │        │  │  ├─ hr.a2b092cc1147.js
│  │        │  │  ├─ hr.a2b092cc1147.js.gz
│  │        │  │  ├─ hr.js
│  │        │  │  ├─ hr.js.gz
│  │        │  │  ├─ hsb.fa3b55265efe.js
│  │        │  │  ├─ hsb.fa3b55265efe.js.gz
│  │        │  │  ├─ hsb.js
│  │        │  │  ├─ hsb.js.gz
│  │        │  │  ├─ hu.6ec6039cb8a3.js
│  │        │  │  ├─ hu.6ec6039cb8a3.js.gz
│  │        │  │  ├─ hu.js
│  │        │  │  ├─ hu.js.gz
│  │        │  │  ├─ hy.c7babaeef5a6.js
│  │        │  │  ├─ hy.c7babaeef5a6.js.gz
│  │        │  │  ├─ hy.js
│  │        │  │  ├─ hy.js.gz
│  │        │  │  ├─ id.04debded514d.js
│  │        │  │  ├─ id.04debded514d.js.gz
│  │        │  │  ├─ id.js
│  │        │  │  ├─ id.js.gz
│  │        │  │  ├─ is.3ddd9a6a97e9.js
│  │        │  │  ├─ is.3ddd9a6a97e9.js.gz
│  │        │  │  ├─ is.js
│  │        │  │  ├─ is.js.gz
│  │        │  │  ├─ it.be4fe8d365b5.js
│  │        │  │  ├─ it.be4fe8d365b5.js.gz
│  │        │  │  ├─ it.js
│  │        │  │  ├─ it.js.gz
│  │        │  │  ├─ ja.170ae885d74f.js
│  │        │  │  ├─ ja.170ae885d74f.js.gz
│  │        │  │  ├─ ja.js
│  │        │  │  ├─ ja.js.gz
│  │        │  │  ├─ ka.2083264a54f0.js
│  │        │  │  ├─ ka.2083264a54f0.js.gz
│  │        │  │  ├─ ka.js
│  │        │  │  ├─ ka.js.gz
│  │        │  │  ├─ km.c23089cb06ca.js
│  │        │  │  ├─ km.c23089cb06ca.js.gz
│  │        │  │  ├─ km.js
│  │        │  │  ├─ km.js.gz
│  │        │  │  ├─ ko.e7be6c20e673.js
│  │        │  │  ├─ ko.e7be6c20e673.js.gz
│  │        │  │  ├─ ko.js
│  │        │  │  ├─ ko.js.gz
│  │        │  │  ├─ lt.23c7ce903300.js
│  │        │  │  ├─ lt.23c7ce903300.js.gz
│  │        │  │  ├─ lt.js
│  │        │  │  ├─ lt.js.gz
│  │        │  │  ├─ lv.08e62128eac1.js
│  │        │  │  ├─ lv.08e62128eac1.js.gz
│  │        │  │  ├─ lv.js
│  │        │  │  ├─ lv.js.gz
│  │        │  │  ├─ mk.dabbb9087130.js
│  │        │  │  ├─ mk.dabbb9087130.js.gz
│  │        │  │  ├─ mk.js
│  │        │  │  ├─ mk.js.gz
│  │        │  │  ├─ ms.4ba82c9a51ce.js
│  │        │  │  ├─ ms.4ba82c9a51ce.js.gz
│  │        │  │  ├─ ms.js
│  │        │  │  ├─ ms.js.gz
│  │        │  │  ├─ nb.da2fce143f27.js
│  │        │  │  ├─ nb.da2fce143f27.js.gz
│  │        │  │  ├─ nb.js
│  │        │  │  ├─ nb.js.gz
│  │        │  │  ├─ ne.3d79fd3f08db.js
│  │        │  │  ├─ ne.3d79fd3f08db.js.gz
│  │        │  │  ├─ ne.js
│  │        │  │  ├─ ne.js.gz
│  │        │  │  ├─ nl.997868a37ed8.js
│  │        │  │  ├─ nl.997868a37ed8.js.gz
│  │        │  │  ├─ nl.js
│  │        │  │  ├─ nl.js.gz
│  │        │  │  ├─ pl.6031b4f16452.js
│  │        │  │  ├─ pl.6031b4f16452.js.gz
│  │        │  │  ├─ pl.js
│  │        │  │  ├─ pl.js.gz
│  │        │  │  ├─ ps.38dfa47af9e0.js
│  │        │  │  ├─ ps.38dfa47af9e0.js.gz
│  │        │  │  ├─ ps.js
│  │        │  │  ├─ ps.js.gz
│  │        │  │  ├─ pt-BR.e1b294433e7f.js
│  │        │  │  ├─ pt-BR.e1b294433e7f.js.gz
│  │        │  │  ├─ pt-BR.js
│  │        │  │  ├─ pt-BR.js.gz
│  │        │  │  ├─ pt.33b4a3b44d43.js
│  │        │  │  ├─ pt.33b4a3b44d43.js.gz
│  │        │  │  ├─ pt.js
│  │        │  │  ├─ pt.js.gz
│  │        │  │  ├─ ro.f75cb460ec3b.js
│  │        │  │  ├─ ro.f75cb460ec3b.js.gz
│  │        │  │  ├─ ro.js
│  │        │  │  ├─ ro.js.gz
│  │        │  │  ├─ ru.934aa95f5b5f.js
│  │        │  │  ├─ ru.934aa95f5b5f.js.gz
│  │        │  │  ├─ ru.js
│  │        │  │  ├─ ru.js.gz
│  │        │  │  ├─ sk.33d02cef8d11.js
│  │        │  │  ├─ sk.33d02cef8d11.js.gz
│  │        │  │  ├─ sk.js
│  │        │  │  ├─ sk.js.gz
│  │        │  │  ├─ sl.131a78bc0752.js
│  │        │  │  ├─ sl.131a78bc0752.js.gz
│  │        │  │  ├─ sl.js
│  │        │  │  ├─ sl.js.gz
│  │        │  │  ├─ sq.5636b60d29c9.js
│  │        │  │  ├─ sq.5636b60d29c9.js.gz
│  │        │  │  ├─ sq.js
│  │        │  │  ├─ sq.js.gz
│  │        │  │  ├─ sr-Cyrl.f254bb8c4c7c.js
│  │        │  │  ├─ sr-Cyrl.f254bb8c4c7c.js.gz
│  │        │  │  ├─ sr-Cyrl.js
│  │        │  │  ├─ sr-Cyrl.js.gz
│  │        │  │  ├─ sr.5ed85a48f483.js
│  │        │  │  ├─ sr.5ed85a48f483.js.gz
│  │        │  │  ├─ sr.js
│  │        │  │  ├─ sr.js.gz
│  │        │  │  ├─ sv.7a9c2f71e777.js
│  │        │  │  ├─ sv.7a9c2f71e777.js.gz
│  │        │  │  ├─ sv.js
│  │        │  │  ├─ sv.js.gz
│  │        │  │  ├─ th.f38c20b0221b.js
│  │        │  │  ├─ th.f38c20b0221b.js.gz
│  │        │  │  ├─ th.js
│  │        │  │  ├─ th.js.gz
│  │        │  │  ├─ tk.7c572a68c78f.js
│  │        │  │  ├─ tk.7c572a68c78f.js.gz
│  │        │  │  ├─ tk.js
│  │        │  │  ├─ tk.js.gz
│  │        │  │  ├─ tr.b5a0643d1545.js
│  │        │  │  ├─ tr.b5a0643d1545.js.gz
│  │        │  │  ├─ tr.js
│  │        │  │  ├─ tr.js.gz
│  │        │  │  ├─ uk.8cede7f4803c.js
│  │        │  │  ├─ uk.8cede7f4803c.js.gz
│  │        │  │  ├─ uk.js
│  │        │  │  ├─ uk.js.gz
│  │        │  │  ├─ vi.097a5b75b3e1.js
│  │        │  │  ├─ vi.097a5b75b3e1.js.gz
│  │        │  │  ├─ vi.js
│  │        │  │  ├─ vi.js.gz
│  │        │  │  ├─ zh-CN.2cff662ec5f9.js
│  │        │  │  ├─ zh-CN.2cff662ec5f9.js.gz
│  │        │  │  ├─ zh-CN.js
│  │        │  │  ├─ zh-CN.js.gz
│  │        │  │  ├─ zh-TW.04554a227c2b.js
│  │        │  │  ├─ zh-TW.04554a227c2b.js.gz
│  │        │  │  ├─ zh-TW.js
│  │        │  │  └─ zh-TW.js.gz
│  │        │  ├─ LICENSE.f94142512c91.md
│  │        │  ├─ LICENSE.f94142512c91.md.gz
│  │        │  ├─ LICENSE.md
│  │        │  ├─ LICENSE.md.gz
│  │        │  ├─ select2.full.c2afdeda3058.js
│  │        │  ├─ select2.full.c2afdeda3058.js.gz
│  │        │  ├─ select2.full.js
│  │        │  ├─ select2.full.js.gz
│  │        │  ├─ select2.full.min.fcd7500d8e13.js
│  │        │  ├─ select2.full.min.fcd7500d8e13.js.gz
│  │        │  ├─ select2.full.min.js
│  │        │  └─ select2.full.min.js.gz
│  │        └─ xregexp
│  │           ├─ LICENSE.b6fd2ceea8d3.txt
│  │           ├─ LICENSE.b6fd2ceea8d3.txt.gz
│  │           ├─ LICENSE.txt
│  │           ├─ LICENSE.txt.gz
│  │           ├─ xregexp.a7e08b0ce686.js
│  │           ├─ xregexp.a7e08b0ce686.js.gz
│  │           ├─ xregexp.js
│  │           ├─ xregexp.js.gz
│  │           ├─ xregexp.min.f1ae4617847c.js
│  │           ├─ xregexp.min.f1ae4617847c.js.gz
│  │           ├─ xregexp.min.js
│  │           └─ xregexp.min.js.gz
│  ├─ css
│  │  ├─ style.css
│  │  └─ style.d41d8cd98f00.css
│  ├─ django-browser-reload
│  │  ├─ reload-listener.b0e8aef308a5.js
│  │  ├─ reload-listener.b0e8aef308a5.js.gz
│  │  ├─ reload-listener.js
│  │  ├─ reload-listener.js.gz
│  │  ├─ reload-worker.04768690f8a1.js
│  │  ├─ reload-worker.04768690f8a1.js.gz
│  │  ├─ reload-worker.js
│  │  └─ reload-worker.js.gz
│  └─ staticfiles.json
├─ templates
│  ├─ 404.html
│  ├─ components
│  │  ├─ doctor_card.html
│  │  └─ form.html
│  ├─ layouts
│  │  └─ base.html
│  ├─ pages
│  │  ├─ about.html
│  │  ├─ contact.html
│  │  ├─ doctor
│  │  │  ├─ appointments.html
│  │  │  ├─ dashboard.html
│  │  │  ├─ doctor_profile.html
│  │  │  ├─ earning.html
│  │  │  ├─ my_patients.html
│  │  │  ├─ patient_profile.html
│  │  │  └─ write_prescription.html
│  │  ├─ doctor.html
│  │  ├─ doctor_details.html
│  │  ├─ index.html
│  │  ├─ login.html
│  │  ├─ patient
│  │  │  ├─ create_allergy.html
│  │  │  ├─ create_family_medical_history.html
│  │  │  ├─ create_medical_history.html
│  │  │  ├─ create_medical_report.html
│  │  │  ├─ dashboard.html
│  │  │  ├─ medical_history.html
│  │  │  ├─ medical_report.html
│  │  │  ├─ medical_report_detail.html
│  │  │  ├─ my_appointments.html
│  │  │  ├─ my_prescriptions.html
│  │  │  ├─ patient_profile.html
│  │  │  ├─ payment_history.html
│  │  │  └─ prescription_detail.html
│  │  ├─ register.html
│  │  ├─ services.html
│  │  └─ video_call.html
│  └─ partials
│     ├─ footer.html
│     ├─ messages.html
│     ├─ navbar.html
│     ├─ pagination.html
│     └─ side_navbar.html
├─ uv.lock
└─ vercel.json

```