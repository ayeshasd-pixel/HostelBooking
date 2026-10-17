import customtkinter as ctk
from tkcalendar import Calendar


# -----------------------------
# App settings
# -----------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Hostel Booking")
app.geometry("1000x800")
app.resizable(False, False)


# -----------------------------
# Hostel data
# -----------------------------
hostels = [
    ("Adhyaman", "Boys Hostel", "₹8,000/month"),
    ("Paari", "Boys Hostel", "₹8,000/month"),
    ("Oori", "Boys Hostel", "₹8,000/month"),
    ("Agasthiyar", "Boys Hostel", "₹8,000/month"),
    ("Kalpana Chawla", "Girls Hostel", "₹8,000/month"),
    ("Malligai", "Girls Hostel", "₹8,000/month"),
    ("Senbegam", "Girls Hostel", "₹8,000/month"),
    ("Thamarai", "Girls Hostel", "₹8,000/month"),
    ("Esq", "Girls Hostel", "₹8,000/month")
]


# -----------------------------
# Page container
# -----------------------------
page_container = ctk.CTkFrame(app, fg_color="transparent")
page_container.pack(fill="both", expand=True)


def clear_page():
    """Remove everything from the current page."""
    for widget in page_container.winfo_children():
        widget.destroy()


def make_back_button(command):
    return ctk.CTkButton(
        page_container,
        text="← Back",
        width=110,
        height=35,
        command=command
    )


# -----------------------------
# Home page
# -----------------------------
def show_home():
    clear_page()

    title = ctk.CTkLabel(
        page_container,
        text="Hostel Booking",
        font=("Impact", 36)
    )
    title.pack(pady=40)

    subtitle = ctk.CTkLabel(
        page_container,
        text="Find your perfect hostel stay",
        font=("Arial", 18)
    )
    subtitle.pack()

    intro = ctk.CTkLabel(
        page_container,
        text="Find your stay near SRM KTR\nComfortable • Affordable • Student Friendly",
        font=("Arial", 18),
        justify="center"
    )
    intro.pack(pady=25)

    popular = ctk.CTkLabel(
        page_container,
        text="Choose Hostel Type",
        font=("Helvetica Neue", 24, "normal")
    )
    popular.pack(pady=15)

    category_frame = ctk.CTkFrame(
        page_container,
        fg_color="transparent"
    )
    category_frame.pack(pady=20)

    boys_button = ctk.CTkButton(
        category_frame,
        text="🧑 Boys Hostels",
        width=250,
        height=60,
        font=("Impact", 20),
        command=lambda: show_hostels("Boys Hostel")
    )
    boys_button.grid(row=0, column=0, padx=20)

    girls_button = ctk.CTkButton(
        category_frame,
        text="👩 Girls Hostels",
        width=250,
        height=60,
        font=("Impact", 20),
        command=lambda: show_hostels("Girls Hostel")
    )
    girls_button.grid(row=0, column=1, padx=20)

    why_title = ctk.CTkLabel(
        page_container,
        text="Why Choose Us?",
        font=("Helvetica Neue", 36, "normal")
    )
    why_title.pack(pady=(40, 20))

    why_frame = ctk.CTkFrame(
        page_container,
        fg_color="transparent"
    )
    why_frame.pack()

    features = [
        "🏠\nMultiple Hostels\n\nChoose from boys & girls hostels",
        "🔒\nSafe & Secure\n\nStudent-friendly stays",
        "⭐\nVerified Ratings\n\nCheck ratings before booking"
    ]

    for i, feature in enumerate(features):
        label = ctk.CTkLabel(
            why_frame,
            text=feature,
            font=("Arial", 16),
            justify="center",
            width=220,
            height=130
        )
        label.grid(row=0, column=i, padx=15)


# -----------------------------
# Hostel list page
# -----------------------------
def show_hostels(hostel_type):
    clear_page()

    make_back_button(show_home).pack(
        anchor="w",
        padx=30,
        pady=(20, 0)
    )

    title = ctk.CTkLabel(
        page_container,
        text=hostel_type,
        font=("Arial", 28, "bold")
    )
    title.pack(pady=20)

    selected_hostels = [
        hostel for hostel in hostels
        if hostel[1] == hostel_type
    ]

    for hostel in selected_hostels:
        create_hostel_card(
            page_container,
            hostel[0],
            hostel[1],
            hostel[2]
        )


# -----------------------------
# Hostel card
# -----------------------------
def create_hostel_card(parent, hostel_name, hostel_type, price):
    card = ctk.CTkFrame(
        parent,
        width=700,
        height=105,
        corner_radius=15
    )
    card.pack(pady=7)
    card.pack_propagate(False)

    name = ctk.CTkLabel(
        card,
        text=hostel_name,
        font=("Helvetica Neue", 20, "normal")
    )
    name.place(x=20, y=12)

    details = ctk.CTkLabel(
        card,
        text=f"{hostel_type} • {price}",
        font=("Arial", 14)
    )
    details.place(x=20, y=45)

    rating = ctk.CTkLabel(
        card,
        text="★ 4.5 / 5",
        font=("Arial", 13, "bold")
    )
    rating.place(x=20, y=73)

    view_button = ctk.CTkButton(
        card,
        text="View Hostel",
        width=130,
        height=35,
        command=lambda: view_hostel_details(
            hostel_name,
            hostel_type,
            price
        )
    )
    view_button.place(x=540, y=34)


# -----------------------------
# Hostel details page
# -----------------------------
def view_hostel_details(hostel_name, hostel_type, price):
    clear_page()

    make_back_button(
        lambda: show_hostels(hostel_type)
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 0)
    )

    name = ctk.CTkLabel(
        page_container,
        text=hostel_name,
        font=("Arial", 30, "bold")
    )
    name.pack(pady=50)

    info = ctk.CTkLabel(
        page_container,
        text=f"{hostel_type}\n{price}\n\nWi-Fi • Food • Laundry • 24/7 Security",
        font=("Arial", 18),
        justify="center"
    )
    info.pack(pady=10)

    book_now = ctk.CTkButton(
        page_container,
        text="Book Now",
        width=200,
        height=45,
        command=lambda: book_hostel(
            hostel_name,
            hostel_type,
            price
        )
    )
    book_now.pack(pady=30)

    page_container.bind(
        "<Return>",
        lambda event: book_hostel(hostel_name, hostel_type, price)
    )
    page_container.focus_set()


# -----------------------------
# Booking page
# -----------------------------
def book_hostel(hostel_name, hostel_type, price):
    clear_page()

    make_back_button(
        lambda: view_hostel_details(hostel_name, hostel_type, price)
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 0)
    )

    title = ctk.CTkLabel(
        page_container,
        text="Hostel Booking",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=25)

    form = ctk.CTkFrame(
        page_container,
        fg_color="transparent"
    )
    form.pack()

    ctk.CTkLabel(
        form,
        text="Student Name"
    ).grid(row=0, column=0, sticky="w", pady=6)

    name_entry = ctk.CTkEntry(
        form,
        width=350,
        placeholder_text="Enter your name"
    )
    name_entry.grid(row=1, column=0, pady=3)

    ctk.CTkLabel(
        form,
        text="Phone Number"
    ).grid(row=2, column=0, sticky="w", pady=6)

    phone_entry = ctk.CTkEntry(
        form,
        width=350,
        placeholder_text="Enter your phone number"
    )
    phone_entry.grid(row=3, column=0, pady=3)

    ctk.CTkLabel(
        form,
        text="Email"
    ).grid(row=4, column=0, sticky="w", pady=6)

    email_entry = ctk.CTkEntry(
        form,
        width=350,
        placeholder_text="Enter your email"
    )
    email_entry.grid(row=5, column=0, pady=3)

    ctk.CTkLabel(
        form,
        text="Room Type"
    ).grid(row=6, column=0, sticky="w", pady=6)

    room_option = ctk.CTkOptionMenu(
        form,
        values=[
            "Single Room",
            "2 Sharing",
            "3 Sharing",
            "4 Sharing"
        ],
        width=350
    )
    room_option.grid(row=7, column=0, pady=3)

    ctk.CTkLabel(
        form,
        text="Move-in Date"
    ).grid(row=8, column=0, sticky="w", pady=6)

    date_entry = ctk.CTkEntry(
        form,
        width=350,
        placeholder_text="Select move-in date"
    )
    date_entry.grid(row=9, column=0, pady=3)

    # Calendar is kept as a small date picker popup,
    # while all actual app steps remain inside the same main window.
    def open_calendar():
        calendar_window = ctk.CTkToplevel(app)
        calendar_window.title("Select Move-in Date")
        calendar_window.geometry("350x350")
        calendar_window.grab_set()

        cal = Calendar(
            calendar_window,
            selectmode="day",
            date_pattern="dd/mm/yyyy",
            background="black",
            foreground="white",
            headersbackground="black",
            headersforeground="white",
            selectbackground="#2196F3",
            selectforeground="white",
            cursor="hand2",
            normalbackground="black",
            normalforeground="white",
            weekendbackground="black",
            weekendforeground="white",
            othermonthbackground="black",
            othermonthforeground="#777777",
            othermonthwebackground="black",
            othermonthweforeground="#555555",
            bordercolor="black",
            disableddaybackground="black",
            disableddayforeground="#555555"
        )

        cal.pack(padx=20, pady=20)

        def select_date():
            selected_date = cal.get_date()
            date_entry.delete(0, "end")
            date_entry.insert(0, selected_date)
            calendar_window.destroy()

        select_button = ctk.CTkButton(
            calendar_window,
            text="Select Date",
            command=select_date
        )
        select_button.pack(pady=10)

    calendar_button = ctk.CTkButton(
        form,
        text="📅 Choose Date",
        width=200,
        height=40,
        command=open_calendar
    )
    calendar_button.grid(row=10, column=0, pady=6)

    error_label = ctk.CTkLabel(
        form,
        text="",
        text_color="red",
        font=("Arial", 14)
    )
    error_label.grid(row=11, column=0, pady=2)

    def confirm_booking():
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()
        date = date_entry.get().strip()

        if not name or not phone or not email or not date:
            error_label.configure(
                text="Please enter all details!"
            )
            return

        show_confirmation(
            hostel_name,
            name,
            phone,
            email,
            room_option.get(),
            date
        )

    confirm_button = ctk.CTkButton(
        form,
        text="Confirm Booking",
        width=200,
        height=45,
        command=confirm_booking
    )
    confirm_button.grid(row=12, column=0, pady=15)

    page_container.bind(
        "<Return>",
        lambda event: confirm_booking()
    )
    page_container.focus_set()


# -----------------------------
# Confirmation page
# -----------------------------
def show_confirmation(
    hostel_name,
    name,
    phone,
    email,
    room_type,
    date
):
    clear_page()

    message = ctk.CTkLabel(
        page_container,
        text="Booking Confirmed! 🎉",
        font=("Impact", 30)
    )
    message.pack(pady=45)

    booking_info = (
        f"Hostel: {hostel_name}\n\n"
        f"Student Name: {name}\n"
        f"Phone Number: {phone}\n"
        f"Email: {email}\n"
        f"Room Type: {room_type}\n"
        f"Move-in Date: {date}"
    )

    details = ctk.CTkLabel(
        page_container,
        text=booking_info,
        font=("Arial", 16),
        justify="left"
    )
    details.pack(pady=15)

    home_button = ctk.CTkButton(
        page_container,
        text="Back to Home",
        width=200,
        height=45,
        command=show_home
    )
    home_button.pack(pady=30)


# Start the app
show_home()
app.mainloop()

