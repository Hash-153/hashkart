"""
NovaMart Comprehensive Catalog Specifications & Technical Attribute Taxonomy
=============================================================================
Defines verified technical specifications and attribute dictionaries across hundreds of consumer SKUs.
"""

from typing import Dict, List


DETAILED_CATALOG_TAXONOMY: List[Dict[str, any]] = [
    {
        "category": "Smartphones & Mobile Devices",
        "hsn": "85171300",
        "specs_schema": [
            "Network & Connectivity (5G Bands, Wi-Fi 6E/7, Bluetooth 5.3, NFC, Ultra Wideband)",
            "Display (LTPO AMOLED, Peak Brightness nits, Refresh Rate, Corning Gorilla Glass Victus 2)",
            "Processor & Architecture (SoC, Fabrication Node, CPU Cores, GPU, NPU TOPS)",
            "Memory & Storage (LPDDR5X RAM, UFS 4.0 Storage, MicroSD Expandability)",
            "Rear Camera System (Main Sensor, Sensor Size, Aperture, OIS, Ultra-Wide, Periscope Telephoto Zoom)",
            "Front Camera (Sensor, Autofocus, 4K60 Video)",
            "Audio (Stereo Speakers, Dolby Atmos, Hi-Res Audio Wireless)",
            "Battery & Charging (Capacity mAh, Wired Fast Charge Wattage, Wireless Qi2 / MagSafe, Reverse Wireless)",
            "Build & Durability (Frame Material, Water & Dust Ingress Protection IP68, Weight grams)",
            "Software & Security (OS Version, Promised Android OS Updates, Security Patch Years, Biometrics)"
        ]
    },
    {
        "category": "Laptops & High-Performance Computing",
        "hsn": "84713010",
        "specs_schema": [
            "Processor (Generation, Base Clock, Boost Clock, Total Cores, Performance Cores, Efficient Cores, L3 Cache)",
            "Graphics Coprocessor (Dedicated GPU, VRAM Type, Total Graphics Power TGP Wattage, MUX Switch, G-Sync)",
            "System Memory (Installed RAM, Bus Speed MHz, Channel Configuration, Max Supported RAM)",
            "Internal Storage (SSD Interface PCIe Gen4/Gen5 NVMe, M.2 Expansion Slots)",
            "Display Technology (Aspect Ratio, Resolution, Refresh Rate, Color Gamut DCI-P3 / sRGB %, Brightness nits, Response Time)",
            "Thermal Management (Vapor Chamber, Dual Liquid Crystal Polymer Fans, Liquid Metal Thermal Compound)",
            "Keyboard & Trackpad (Per-Key RGB / White Backlit, Key Travel mm, Glass Precision Touchpad)",
            "Port Selection (Thunderbolt 4 / USB4, USB 3.2 Gen2 Type-A, HDMI 2.1 FRL, SD Express 7.0 Card Reader, Audio Combo Jack)",
            "Battery & Power Adapter (Watt-Hours, Fast Charge 50% in 30 mins, USB-C PD Charging Support)",
            "Chassis Construction (CNC Anodized Aluminum / Magnesium Alloy, Military Grade MIL-STD-810H Certified, Weight kg)"
        ]
    },
    {
        "category": "Smart Televisions & Home Theatre",
        "hsn": "85287200",
        "specs_schema": [
            "Panel Technology (OLED / QD-OLED / Mini-LED / QLED, Native Refresh Rate Hz, Local Dimming Zones)",
            "Video Engine (AI Neural Picture Engine, HDR10+, Dolby Vision IQ, Filmmaker Mode, MEMC)",
            "Gaming Capabilities (HDMI 2.1 4K120/144Hz, Auto Low Latency Mode ALLM, VRR, FreeSync Premium Pro, Game Bar)",
            "Audio Specifications (Total Output Watts, Channel Configuration, Dolby Atmos, DTS:X, Acoustic Surface Audio)",
            "Smart Platform (Google TV / webOS / Tizen OS, Voice Assistants Built-in, Apple AirPlay 2 / Chromecast)",
            "Connectivity (Dual-Band Wi-Fi, Bluetooth, Optical Digital Audio Out, eARC Port, Ethernet LAN)",
            "Power Consumption (Operating Watts, Standby Watts, Energy Star Star Rating)"
        ]
    },
    {
        "category": "Inverter Air Conditioners & HVAC",
        "hsn": "84151010",
        "specs_schema": [
            "Cooling Capacity (Rated Capacity Watts, Tonnage, ISEER Star Rating, Annual Energy Consumption kWh)",
            "Compressor Technology (Dual Rotary Inverter / Variable Speed Tropical Compressor, Ambient Operating Temp °C)",
            "Condenser & Evaporator (100% Grooved Inner Copper Tubes, Anti-Corrosive Blue/Gold Fin Coating)",
            "Air Filtration (PM 2.5 Filter, Anti-Bacterial Micro Dust Filter, Self-Clean Frost Wash)",
            "Smart Features (Wi-Fi App Control, Voice Commands Alexa/Google, AI Auto Cooling Sensor)",
            "Refrigerant (Eco-Friendly R32 Zero Ozone Depletion Potential)",
            "Noise Level (Indoor Unit Quiet Mode dBA, Outdoor Unit dBA)"
        ]
    },
    {
        "category": "Audio & Premium Headphones",
        "hsn": "85183000",
        "specs_schema": [
            "Acoustic Design (Custom Carbon Fiber Dynamic Driver mm, Frequency Response Hz - kHz, Impedance Ohms, Sensitivity dB)",
            "Active Noise Cancellation (Multi-Microphone Hybrid ANC, Ambient Transparency Level Steps, Wind Noise Reduction)",
            "Wireless Protocol (Bluetooth Version, Supported Codecs LDAC, aptX Adaptive, LC3, AAC, SBC, Multipoint 2-Device Pairing)",
            "Battery Performance (Playback Time with ANC On/Off, Case Battery Hours, USB-C Fast Charge 10 min for 5 hours)",
            "Microphone System (Beamforming Array, Bone Conduction Sensor, AI Clear Voice Pickup)",
            "Ingress Protection (Sweat & Splash Proof IPX4 / IP55)",
            "Companion App (Custom 10-Band Graphic Equalizer, Spatial Audio with Dynamic Head Tracking, Hearing Profile Calibration)"
        ]
    }
]
