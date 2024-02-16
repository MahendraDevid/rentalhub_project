from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect ke halaman yang sesuai tergantung pada peran pengguna (admin/pembeli)
            if user.is_superuser:
                return redirect('admin_dashboard')  # Ganti dengan nama URL untuk dashboard admin
            else:
                return redirect('pembeli_dashboard')  # Ganti dengan nama URL untuk dashboard pembeli
        else:
            # Handle login gagal (misalnya, tampilkan pesan kesalahan)
            return render(request, 'users/login.html', {'error': 'Username atau password salah'})
    else:
        return render(request, 'users/login.html')
