import torch

if torch.cuda.is_available():
    print("✅ Sukses! GPU NVIDIA terdeteksi oleh PyTorch.")
    print(f"Nama GPU: {torch.cuda.get_device_name(0)}")
    try:
        device = torch.device("cuda")
        tensor_gpu = torch.randn(3, 3).to(device)
        print("\nBerhasil membuat sebuah tensor langsung di GPU:")
        print(tensor_gpu)
        print(f"Lokasi tensor saat ini: {tensor_gpu.device}")
    except Exception as e:
        print(f"Gagal saat mencoba membuat tensor di GPU. Error: {e}")

else:
    print("❌ Gagal! PyTorch tidak dapat mendeteksi GPU Anda.")
    print("Pastikan semua langkah instalasi Driver, CUDA, dan PyTorch versi GPU sudah benar.")

print(torch.__version__)