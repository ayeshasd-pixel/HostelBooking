import customtkinter as ctk
from tkcalendar import Calendar

def view_hostel_details(hostel_name, hostel_type, price):

    # Create hostel details page inside the main window
    details_page = ctk.CTkFrame(
        main_container,
        fg_color="transparent"
    )

    name = ctk.CTkLabel(
        details_page,
        text=hostel_name,
        font=("Arial", 30, "bold")
    )
    name.pack(pady=40)

    info = ctk.CTkLabel(
        details_page,
        text=f"{hostel_type}\n{price}\n\nWi-Fi • Food • Laundry • 24/7 Security",
        font=("Arial", 18),
        justify="center"
    )
    info.pack(pady=10)

    book_now = ctk.CTkButton(
        details_page,
        text="Book Now",
        width=200,
        height=45,
        command=lambda: book_hostel(hostel_name)
    )
    book_now.pack(pady=25)

    back_button = ctk.CTkButton(
        details_page,
        text="← Back",
        width=120,
        command=lambda: show_hostels(hostel_type)
    )
    back_button.pack(pady=10)

    app.bind("<Return>", lambda event: book_hostel(hostel_name))
    app.bind("<Escape>", lambda event: show_hostels(hostel_type))

    show_page(details_page)

def book_hostel(hostel_name):

    # Create booking page inside the main window
    booking_page = ctk.CTkFrame(
        main_container,
        fg_color="transparent"
    )

    title = ctk.CTkLabel(
        booking_page,
        text="Hostel Booking",
        font=("Arial", 28, "bold")
    )
    title.pack(pady=30)

    name_label = ctk.CTkLabel(
        booking_page,
        text="Student Name"
    )
    name_label.pack(pady=5)

    name_entry = ctk.CTkEntry(
        booking_page,
        width=350,
        placeholder_text="Enter your name"
    )
    name_entry.pack(pady=5)

    phone_label = ctk.CTkLabel(
        booking_page,
        text="Phone Number"
    )
    phone_label.pack(pady=5)

    phone_entry = ctk.CTkEntry(
        booking_page,
        width=350,
        placeholder_text="Enter your phone number"
    )
    phone_entry.pack(pady=5)

    email_label = ctk.CTkLabel(
        booking_page,
        text="Email"
    )
    email_label.pack(pady=5)

    email_entry = ctk.CTkEntry(
        booking_page,
        width=350,
        placeholder_text="Enter your email"
    )
    email_entry.pack(pady=5)

    room_label = ctk.CTkLabel(
        booking_page,
        text="Room Type"
    )
    room_label.pack(pady=5)

    room_option = ctk.CTkOptionMenu(
        booking_page,
        values=["Single Room", "2 Sharing", "3 Sharing", "4 Sharing"]
    )
    room_option.pack(pady=5)

    date_label = ctk.CTkLabel(
        booking_page,
        text="Move-in Date"
    )
    date_label.pack(pady=5)

    date_entry = ctk.CTkEntry(
        booking_page,
        width=350,
        placeholder_text="Select move-in date"
    )
    date_entry.pack(pady=5)

    def open_calendar():

        calendar_page = ctk.CTkFrame(
            main_container,
            fg_color="transparent"
        )

        calendar_title = ctk.CTkLabel(
            calendar_page,
            text="Select Move-in Date",
            font=("Arial", 28, "bold")
        )
        calendar_title.pack(pady=30)

        cal = Calendar(
            calendar_page,
            selectmode="day",
            date_pattern="dd/mm/yyyy"
        )
        cal.pack(pady=20)

        def select_date():
            selected_date = cal.get_date()

            date_entry.delete(0, "end")
            date_entry.insert(0, selected_date)

            show_page(booking_page)

        select_button = ctk.CTkButton(
            calendar_page,
            text="Select Date",
            width=200,
            height=45,
            command=select_date
        )
        select_button.pack(pady=20)

        back_button = ctk.CTkButton(
            calendar_page,
            text="← Back",
            width=120,
            command=lambda: show_page(booking_page)
        )
        back_button.pack(pady=10)

        app.bind("<Return>", lambda event: select_date())
        app.bind("<Escape>", lambda event: show_page(booking_page))

        show_page(calendar_page)


    calendar_button = ctk.CTkButton(
        booking_page,
        text="📅 Choose Date",
        width=200,
        height=40,
        command=open_calendar
    )
    calendar_button.pack(pady=5)

    def confirm_booking():

        if not name_entry.get() or not phone_entry.get() or not email_entry.get() or not date_entry.get():
            error_label = ctk.CTkLabel(
                booking_page,
                text="⚠️ Please fill in all the details",
                font=("Arial", 16, "bold")
            )
            error_label.pack(pady=10)
            return

        confirmation_page = ctk.CTkFrame(
            main_container,
            fg_color="transparent"
        )

        success_title = ctk.CTkLabel(
            confirmation_page,
            text="🎉 Booking Confirmed!",
            font=("Arial", 30, "bold")
        )
        success_title.pack(pady=40)

        details = ctk.CTkLabel(
            confirmation_page,
            text=f"Hostel: {hostel_name}\n\n"
                f"Student: {name_entry.get()}\n"
                f"Phone: {phone_entry.get()}\n"
                f"Email: {email_entry.get()}\n"
                f"Room: {room_option.get()}\n"
                f"Move-in Date: {date_entry.get()}",
            font=("Arial", 18),
            justify="center"
        )
        details.pack(pady=20)

        back_home = ctk.CTkButton(
            confirmation_page,
            text="Back to Home",
            width=200,
            height=45,
            command=lambda: show_page(home_page)
        )
        back_home.pack(pady=30)

        app.bind("<Escape>", lambda event: show_page(home_page))

        show_page(confirmation_page)

    confirm_button = ctk.CTkButton(
        booking_page,
        text="Confirm Booking",
        width=200,
        height=45,
        command=confirm_booking
    )
    confirm_button.pack(pady=25)

    back_button = ctk.CTkButton(
        booking_page,
        text="← Back",
        width=120,
        command=lambda: view_hostel_details(
            hostel_name,
            "Hostel",
            ""
        )
    )
    back_button.pack(pady=5)

    app.bind("<Return>", lambda event: confirm_booking())
    app.bind("<Escape>", lambda event: view_hostel_details(
        hostel_name,
        "Hostel",
        ""
    ))

    show_page(booking_page)

def search_hostel():
    search_result.configure(text="Hostels found near your location!")

    popular.pack(pady=(10, 5))
    hostel_card.pack(pady=20)
    hostel_card2.pack(pady=10)

# App settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Hostel Booking")
app.geometry("1000x800")
app.resizable(False, False)

# Main page container
main_container = ctk.CTkFrame(app, fg_color="transparent")
main_container.pack(fill="both", expand=True)

# Home page
home_page = ctk.CTkFrame(main_container, fg_color="transparent")

# Function to switch pages
def show_page(page):
    for widget in main_container.winfo_children():
        widget.pack_forget()
        widget.grid_forget()
        widget.place_forget()

    page.pack(fill="both", expand=True)

# Heading
title = ctk.CTkLabel(
    home_page,
    text="Hostel Booking",
    font=("Impact", 36)
)
title.pack(pady=40)

# Subtitle
subtitle = ctk.CTkLabel(
    home_page,
    text="Find your perfect hostel stay",
    font=("Arial", 18)
)
subtitle.pack()

intro = ctk.CTkLabel(
    home_page,
    text="Find your stay near SRM KTR\nComfortable • Affordable • Student Friendly",
    font=("Arial", 18),
    justify="center"
)
intro.pack(pady=25)

popular = ctk.CTkLabel(
    home_page,
    text="Popular Hostels",
    font=("Helvetica Neue", 24, "normal")
)
popular.pack(pady=10)

# Hostel data
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


# Function to create hostel cards
def create_hostel_card(parent, hostel_name, hostel_type, price):

    card = ctk.CTkFrame(
        parent,
        width=600,
        height=120,
        corner_radius=15
    )

    card.pack(pady=8)
    card.pack_propagate(False)

    name = ctk.CTkLabel(
        card,
        text=hostel_name,
        font=("Helvetica Neue", 20, "normal")
    )
    name.place(x=20, y=15)

    details = ctk.CTkLabel(
        card,
        text=f"{hostel_type} • {price}",
        font=("Arial", 14)
    )
    details.place(x=20, y=50)

    rating = ctk.CTkLabel(
        card,
        text="★ 4.5 / 5",
        font=("Arial", 13, "bold")
    )
    rating.place(x=20, y=82)

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
    view_button.place(x=440, y=40)

    return card

# Function to show hostel list
def show_hostels(hostel_type):

    # Create hostel list page inside the main window
    hostel_page = ctk.CTkFrame(main_container, fg_color="transparent")

    title = ctk.CTkLabel(
        hostel_page,
        text=hostel_type,
        font=("Arial", 28, "bold")
    )
    title.pack(pady=20)

    # Back button
    back_button = ctk.CTkButton(
        hostel_page,
        text="← Back",
        width=100,
        command=lambda: show_page(home_page)
    )
    back_button.pack(pady=5)

    app.bind("<Escape>", lambda event: back_button.invoke())

    # Filter hostels according to type
    selected_hostels = [
        hostel for hostel in hostels
        if hostel[1] == hostel_type
    ]

    # Create hostel cards
    for hostel in selected_hostels:
        create_hostel_card(
            hostel_page,
            hostel[0],
            hostel[1],
            hostel[2]
        )

    show_page(hostel_page)


# Hostel category buttons

category_frame = ctk.CTkFrame(home_page, fg_color="transparent")
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

# Why Choose Us section

why_title = ctk.CTkLabel(
    home_page,
    text="Why Choose Us?",
    font=("Helvetica Neue", 36, "normal")
)
why_title.pack(pady=(40, 20))

why_frame = ctk.CTkFrame(
    home_page,
    fg_color="transparent"
)
why_frame.pack()

# Multiple Hostels
hostel_feature = ctk.CTkLabel(
    why_frame,
    text="🏠\nMultiple Hostels\n\nChoose from boys & girls hostels",
    font=("Arial", 16),
    justify="center",
    width=220,
    height=130
)
hostel_feature.grid(row=0, column=0, padx=15)

# Safe & Secure
safe_feature = ctk.CTkLabel(
    why_frame,
    text="🔒\nSafe & Secure\n\nStudent-friendly stays",
    font=("Arial", 16),
    justify="center",
    width=220,
    height=130
)
safe_feature.grid(row=0, column=1, padx=15)

# Verified Ratings
rating_feature = ctk.CTkLabel(
    why_frame,
    text="⭐\nVerified Ratings\n\nCheck ratings before booking",
    font=("Arial", 16),
    justify="center",
    width=220,
    height=130
)
rating_feature.grid(row=0, column=2, padx=15)

show_page(home_page)

app.mainloop()