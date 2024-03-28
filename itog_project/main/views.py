from django.shortcuts import render, redirect
from django.views import View
from .models import Offer, WorkerResume, EmployeerResume, Message
from .form import AddOfferForm, WorkerResumeForm, EmployeerResumeForm, MessageForm
from django.contrib.auth.models import User
import os


class MainView(View):
    def get(self, request):
        offers = Offer.objects.filter(is_active=True)
        return render(request, 'main/main.html', {'offers': offers})


class OfferDetailView(View):
    def get(self, request, pk):
        offer = Offer.objects.get(id=pk)
        return render(request, 'main/offer_detail.html', {'offer': offer})


class AddOfferView(View):
    def get(self, request):
        try:
            employeer_resume = EmployeerResume.objects.get(owner=request.user)
        except:
            return redirect('/')
        form = AddOfferForm()
        return render(request, 'main/add_offer.html', {'form': form})

    def post(self, request):
        form = AddOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.owner = request.user
            offer.save()
            return redirect("offer_detail", pk=offer.id)


class DeleteOfferView(View):
    def get(self, request, pk):
        offer = Offer.objects.get(id=pk)
        offer.delete()
        return redirect('/')


class EditOfferView(View):
    def get(self, request, pk):
        offer = Offer.objects.get(id=pk)
        form = AddOfferForm(instance=offer)
        return render(request, 'main/edit_offer.html', {'offer': offer, 'form': form})

    def post(self, request, pk):
        offer = Offer.objects.get(id=pk)
        form = AddOfferForm(data=request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect(f'/detail-{pk}')


class CreateWorkerResumeView(View):
    def get(self, request):
        form = WorkerResumeForm()
        return render(request, 'main/worker_resume.html', {'form': form})

    def post(self, request):
        form = WorkerResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = request.user
            resume.save()
            return redirect('/dashboard')
        return render(request, 'main/worker_resume.html', {'form': form})


class EditWorkerResumeView(View):
    def get(self, request):
        resume = WorkerResume.objects.get(owner=request.user)
        form = WorkerResumeForm(instance=resume)
        return render(request, 'main/edit_worker_resume.html', {'form': form})

    def post(self, request):
        resume = WorkerResume.objects.get(owner=request.user)
        form = WorkerResumeForm(instance=resume, data=request.POST, files=request.FILES)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.owner = request.user
            new_resume.save()
            return redirect('/dashboard')
        return render(request, 'main/edit_worker_resume.html', {'form': form})


class CreateEmployeerResumeView(View):
    def get(self, request):
        form = EmployeerResumeForm()
        return render(request, 'main/employeer_resume.html', {'form': form})

    def post(self, request):
        form = EmployeerResumeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = request.user
            resume.save()
            return redirect('/dashboard')
        return render(request, 'main/employeer_resume.html', {'form': form})


class EditEmployeerResumeView(View):
    def get(self, request):
        resume = EmployeerResume.objects.get(owner=request.user)
        form = EmployeerResumeForm(instance=resume)
        return render(request, 'main/edit_employeer_resume.html', {'form': form})

    def post(self, request):
        resume = EmployeerResume.objects.get(owner=request.user)
        form = EmployeerResumeForm(instance=resume, data=request.POST, files=request.FILES)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.owner = request.user
            new_resume.save()
            return redirect('/dashboard')
        return render(request, 'main/edit_employeer_resume.html', {'form': form})


class DashboardView(View):
    def get(self, request):
        user_offers = Offer.objects.filter(owner=request.user)
        context = {'offers': user_offers}
        worker_resume = WorkerResume.objects.filter(owner=request.user)
        employeer_resume = EmployeerResume.objects.filter(owner=request.user)
        if worker_resume:
            worker_resume = worker_resume[0]
            context['worker_resume'] = worker_resume
        elif employeer_resume:
            employeer_resume = employeer_resume[0]
            context['employeer_resume'] = employeer_resume

        return render(request, 'main/dashboard.html', context)


class UserProfileView(View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        if user == request.user:
            return redirect('/dashboard')

        context = {'username': user.username}
        worker_resume = WorkerResume.objects.filter(owner=user)
        employeer_resume = EmployeerResume.objects.filter(owner=user)
        if worker_resume:
            context['worker_resume'] = worker_resume[0]
        elif employeer_resume:
            context['employeer_resume'] = employeer_resume[0]
        return render(request, 'main/user_profile.html', context)


class ChatView(View):
    def get(self, request, pk):
        user = request.user
        user2 = User.objects.get(id=pk)
        messages = [msg for msg in Message.objects.all()
                    if (msg.sender == user2 and msg.receiver == user and msg.is_read) \
                    or (msg.sender == user and msg.receiver == user2)]
        unread_messages = user.receive_messages.filter(is_read=False)
        for msg in unread_messages:
            msg.is_read = True
            msg.save()
        form = MessageForm()
        return render(request, 'main/chat.html', {'messages': messages, 'user2': user2, 'form': form,
                                                  'unread_messages': unread_messages})

    def post(self, request, pk):
        user = request.user
        user2 = User.objects.get(id=pk)
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = user
            message.receiver = user2
            message.save()

        return redirect(f'/chat-{pk}')


class InputView(View):
    def get(self, request):
        inbox_dct = {}
        all_chats_with_last_msgs = {}
        for msg in Message.objects.all():
            if msg.sender == request.user:
                all_chats_with_last_msgs[msg.receiver] = msg
            elif msg.receiver == request.user:
                all_chats_with_last_msgs[msg.sender] = msg

        all_chats_with_last_msgs = list(all_chats_with_last_msgs.items())
        all_chats_with_last_msgs.reverse()
        for msg in request.user.receive_messages.filter(is_read=False):
            sender = msg.sender
            if sender in inbox_dct:
                inbox_dct[sender] += 1
            else:
                inbox_dct[sender] = 1

        for sender, msg_cnt in inbox_dct.items():
            if msg_cnt % 10 == 1:
                inbox_dct[sender] = f'У вас {msg_cnt} непрочитанное сообщение'
            elif 2 <= msg_cnt % 10 <= 4 and (msg_cnt // 10) % 10 != 1:
                inbox_dct[sender] = f'У вас {msg_cnt} непрочитанных сообщения'
            else:
                inbox_dct[sender] = f'У вас {msg_cnt} непрочитанных сообщений'

        return render(request, 'main/input.html', {'inbox': inbox_dct,
                                                   'all_chats_with_last_msgs': all_chats_with_last_msgs})


class ApplyView(View):
    def get(self, request, pk):
        offer = Offer.objects.get(id=pk)
        message = Message.objects.create(text=f'Отклик на вакансию.\n{offer.job_title}', sender=request.user,
                                         receiver=offer.owner)
        return redirect(f'/chat-{offer.owner.id}')
class SearchView(View):
    def post(self, request):
        query = request.POST['search']
        query = query.strip().lower()
        offers = [offer for offer in Offer.objects.filter(is_active=True)
                  if query in offer.job_title.lower() or offer.job_title.lower() in query]
        return render(request, 'main/main.html', {'offers': offers})

class SortingView(View):
    def post(self, request):
        print(request.POST)
        sorting = request.POST['sorting']
        if sorting == 'date':
            offers = Offer.objects.filter(is_active=True).order_by('date')
        elif sorting == 'salary':
            offers = Offer.objects.filter(is_active=True).order_by('salary')
        elif sorting == 'apply':
            pass
        return redirect('/')