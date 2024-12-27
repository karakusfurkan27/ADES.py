import numpy as np
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class EnergyStorageSystem:
    def __init__(self, capacity, charge_rate, discharge_rate):
        self.capacity = capacity  # kWh
        self.charge_rate = charge_rate  # kW
        self.discharge_rate = discharge_rate  # kW
        self.energy_stored = 0  # kWh

    def charge(self, energy):
        chargeable_energy = min(energy, self.capacity - self.energy_stored)
        self.energy_stored += chargeable_energy
        return chargeable_energy

    def discharge(self, demand):
        dischargeable_energy = min(self.energy_stored, demand)
        self.energy_stored -= dischargeable_energy
        return dischargeable_energy

    def status(self):
        return self.energy_stored

    def storage_efficiency(self, energy_generated):
        if energy_generated > 0:
            return (self.energy_stored / energy_generated) * 100
        return 0

class RenewableEnergySystem:
    def __init__(self, solar_capacity, wind_capacity):
        self.solar_capacity = solar_capacity  # kW
        self.wind_capacity = wind_capacity  # kW

    def generate_solar_energy(self, sunlight_hours):
        return self.solar_capacity * sunlight_hours

    def generate_wind_energy(self, wind_speed):
        return self.wind_capacity * np.clip(wind_speed / 10, 0, 1)

    def generate_forecast(self):
        sunlight_hours = random.uniform(4, 10)
        wind_speed = random.uniform(5, 20)
        return sunlight_hours, wind_speed

    def simulate_outage(self):
        # Kesinti durumu simülasyonu (1 hafta boyunca enerji üretimi sıfırlanacak)
        return 0, 0

class Microgrid:
    def __init__(self, storage_capacity, solar_capacity, wind_capacity):
        self.energy_storage = EnergyStorageSystem(storage_capacity, 10, 10)
        self.renewable_system = RenewableEnergySystem(solar_capacity, wind_capacity)
        self.energy_demand = 0
        self.energy_generated = 0
        self.storage_history = []
        self.generated_history = []
        self.demand_history = []
        self.efficiency_history = []
        self.monthly_consumption = 0
        self.monthly_generation = 0
        self.outage_duration = 0  # Kesinti süresi (gün cinsinden)
        self.outage_active = False  # Kesinti durumu

    def update_energy(self, sunlight_hours, wind_speed, energy_demand, simulate_outage=False):
        if simulate_outage:
            # Kesinti durumunda enerji üretimi sıfırlanır
            sunlight_hours, wind_speed = self.renewable_system.simulate_outage()
            self.outage_active = True
            self.outage_duration += 1
            print(f"Kesinti durumunda {self.outage_duration} gündür enerji üretimi yok.")
        else:
            self.outage_active = False

        self.energy_demand = energy_demand
        solar_energy = self.renewable_system.generate_solar_energy(sunlight_hours)
        wind_energy = self.renewable_system.generate_wind_energy(wind_speed)
        self.energy_generated = solar_energy + wind_energy
        
        # Enerji üretimi sıfırlansa bile depolama devreye girmelidir
        if self.outage_active:
            # Kesinti sırasında enerji depolama ile talep karşılanacak
            energy_supplied = self.energy_storage.discharge(self.energy_demand)
        else:
            # Enerji üretimi varken, enerji depolama devreye girecek
            energy_to_store = self.energy_storage.charge(self.energy_generated)
            energy_supplied = self.energy_storage.discharge(self.energy_demand)

        # Enerji verimliliği hesaplaması
        efficiency = self.energy_storage.storage_efficiency(self.energy_generated)
        self.storage_history.append(self.energy_storage.status())
        self.generated_history.append(self.energy_generated)
        self.demand_history.append(self.energy_demand)
        self.efficiency_history.append(efficiency)

        # Aylık tüketim ve üretim takibi
        self.monthly_consumption += self.energy_demand
        self.monthly_generation += self.energy_generated

    def plot_energy(self, root):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(self.storage_history, label='Depolanan Enerji (kWh)', color='green')
        ax.plot(self.generated_history, label='Üretilen Enerji (kWh)', color='orange')
        ax.plot(self.demand_history, label='Enerji Talebi (kWh)', color='blue')
        ax.set_xlabel('Zaman (gün)')
        ax.set_ylabel('Enerji (kWh)')
        ax.legend()
        ax.set_title('Enerji Üretimi, Talebi ve Depolama Durumu')

        canvas = FigureCanvasTkAgg(fig, master=root)  
        canvas.get_tk_widget().pack()
        canvas.draw()

    def show_monthly_report(self):
        return f"Aylık Tüketim: {self.monthly_consumption:.2f} kWh\nAylık Üretim: {self.monthly_generation:.2f} kWh"

    def show_daily_log(self):
        log = ""
        for i in range(len(self.storage_history)):
            log += f"Gün {i+1} - Depolama Durumu: {self.storage_history[i]:.2f} kWh, Üretilen Enerji: {self.generated_history[i]:.2f} kWh, Enerji Talebi: {self.demand_history[i]:.2f} kWh, Depolama Verimliliği: {self.efficiency_history[i]:.2f}%\n"
        return log

    def show_outage_warning(self):
        if self.outage_active:
            return f"Uyarı: {self.outage_duration} gündür kesinti yaşanıyor."
        return "Kesinti yok."

# GUI oluşturulması
def on_submit():
    try:
        sunlight_hours = float(entry_sunlight_hours.get())
        wind_speed = float(entry_wind_speed.get())
        energy_demand = float(entry_energy_demand.get())
        simulate_outage = outage_check_var.get()

        # Mikro ağ simülasyonu başlatma
        microgrid = Microgrid(storage_capacity=50, solar_capacity=20, wind_capacity=15)
        
        # Enerji verisini güncelle
        microgrid.update_energy(sunlight_hours, wind_speed, energy_demand, simulate_outage)
        
        # Enerji üretimi ve depolama grafiği çiz
        microgrid.plot_energy(root)
        
        # Günlük logu göster
        log_text = microgrid.show_daily_log()
        log_label.config(text=log_text)
        
        # Aylık rapor göster
        monthly_report = microgrid.show_monthly_report()
        monthly_label.config(text=monthly_report)
        
        # Kesinti uyarısını göster
        outage_warning = microgrid.show_outage_warning()
        outage_label.config(text=outage_warning)
        
        messagebox.showinfo("Simülasyon Tamamlandı", "Enerji üretimi ve depolama başarıyla simüle edildi!")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

# Tkinter pencereyi oluşturma
root = tk.Tk()
root.title("Enerji Depolama ve Üretim Simülasyonu")
root.geometry("800x600")
root.configure(bg='#ff5733')

# Arayüz elemanlarını oluşturma
label_sunlight_hours = tk.Label(root, text="Günlük Güneş Işığı Süresi (saat):", bg='#ff5733', font=("Arial", 12))
label_sunlight_hours.pack()

entry_sunlight_hours = tk.Entry(root, font=("Arial", 12))
entry_sunlight_hours.pack()

label_wind_speed = tk.Label(root, text="Rüzgar Hızı (km/saat):", bg='#ff5733', font=("Arial", 12))
label_wind_speed.pack()

entry_wind_speed = tk.Entry(root, font=("Arial", 12))
entry_wind_speed.pack()

label_energy_demand = tk.Label(root, text="Enerji Talebi (kWh):", bg='#ff5733', font=("Arial", 12))
label_energy_demand.pack()

entry_energy_demand = tk.Entry(root, font=("Arial", 12))
entry_energy_demand.pack()

# Kesinti simülasyonu seçeneği
outage_check_var = tk.BooleanVar()
outage_checkbox = tk.Checkbutton(root, text="Kesinti simülasyonu aktif", variable=outage_check_var, bg='#ff5733', font=("Arial", 12))
outage_checkbox.pack()

submit_button = tk.Button(root, text="Simülasyonu Başlat", command=on_submit, font=("Arial", 14), bg="#4caf50", fg="white")
submit_button.pack(pady=20)

log_label = tk.Label(root, text="", bg='#ff5733', font=("Arial", 10), justify="left", anchor="w")
log_label.pack(pady=10)

monthly_label = tk.Label(root, text="", bg='#ff5733', font=("Arial", 10), justify="left", anchor="w")
monthly_label.pack(pady=10)

outage_label = tk.Label(root, text="", bg='#ff5733', font=("Arial", 10), justify="left", anchor="w")
outage_label.pack(pady=10)

# Uygulama penceresini başlatma
root.mainloop()
