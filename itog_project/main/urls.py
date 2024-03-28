from .views import MainView, OfferDetailView, AddOfferView, EditOfferView, \
    DeleteOfferView, CreateWorkerResumeView, CreateEmployeerResumeView, DashboardView, EditEmployeerResumeView, \
    EditWorkerResumeView, UserProfileView, ChatView, InputView, ApplyView, SearchView, SortingView
from django.urls import path, include

urlpatterns = [path('', MainView.as_view(), name='main'),
               path('detail-<int:pk>', OfferDetailView.as_view(), name='offer_detail'),
               path('add_offer', AddOfferView.as_view(), name='add_offer'),
               path('edit-offer-<int:pk>', EditOfferView.as_view(), name='edit_offer'),
               path('delete-offer-<int:pk>', DeleteOfferView.as_view(), name='delete_offer'),
               path('create-worker-resume', CreateWorkerResumeView.as_view(), name='create_worker_resume'),
               path('edit-worker-resume', EditWorkerResumeView.as_view(), name='edit_worker_resume'),
               path('create-employeer-resume', CreateEmployeerResumeView.as_view(), name='create_employeer_resume'),
               path('edit-employeer-resume', EditEmployeerResumeView.as_view(), name='edit_employeer_resume'),
               path('dashboard', DashboardView.as_view(), name='dashboard'),
               path('user-profile-<int:pk>', UserProfileView.as_view(), name='user_profile'),
               path('chat-<int:pk>', ChatView.as_view(), name='chat'),
               path('input', InputView.as_view(), name='input'),
               path('apply-<int:pk>', ApplyView.as_view(), name='apply'),
               path('sorting', SortingView.as_view(), name='sorting'),
               path('search', SearchView.as_view(), name='search')]
