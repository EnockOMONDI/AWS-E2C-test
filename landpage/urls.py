from django.conf.urls import patterns, include, url

from landpage.views import txt
from landpage.views import landpage
from landpage.views import privacy
from landpage.views import terms
from landpage.views import forgot_password
from landpage.views import google
from landpage.views import landpageprod

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = patterns('',
    # Custom Files
    url(r'^robots\.txt$', txt.robots_txt_page, name='robots'),
    url(r'^humans\.txt$', txt.humans_txt_page, name='humans'),
                       
    # Google Verify
    url(r'^googlee81f1c16590924d1.html$', google.google_verify_page, name='google_plus_verify'),
    url(r'^googlee81f1c16590924d1$', google.google_verify_page),
                       
    # Landpage
    url(r'^$',landpageprod.landpageprod_page, name='landpageprod'),
    url(r'^landpage$', landpage.landpage_page),
    url(r'^course_preview_modal$', landpage.course_preview_modal),
    url(r'^save_contact_us_message$', landpage.save_contact_us_message),

     #productionpages
    url(r'^landpageprod$', landpageprod.landpageprod_page, name='landpageprod'),
    url(r'^welcome$', landpageprod.welcome, name='welcome'),
    url(r'^aboutus$', landpageprod.about_us, name='aboutus'),
    url(r'^enrollnow$', landpageprod.enrollnow, name='enrollnow'),
    url(r'^studentfaqs$', landpageprod.studentfaqs, name='studentfaqs'),
    url(r'^sdgfaqs$', landpageprod.sdgfaqs, name='sdgfaqs'),
    url(r'^benefits', landpageprod.benefits, name=' benefits'),
    url(r'^contactus$', landpageprod.contactus, name='contactus'), 
    url(r'^sdgdigitallab$', landpageprod.sdgdigitallab, name='sdgdigitallab'), 
    url(r'^volunteerpage$', landpageprod.volunteer, name='volunteer'),
    url(r'^digitallab$', landpageprod.digitallab , name='digitallab '),
    # url(r'^edit/', views.edit, name='edit'),
                     
    # Off-Convas Stuff
    url(r'^terms$', terms.terms_page, name='terms'),
    url(r'^privacy', privacy.privacy_page, name='privacy'),
    url(r'^forgot_password$', forgot_password.forgot_password_page, name='forgot_password'),
    url(r'^reset_password$', forgot_password.reset_password, name='reset_password'),
                       
    # Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
)

# Captchas
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)