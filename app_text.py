# -*- coding: utf-8 -*-
'''
the app text is structured in dictionaries:

climate_tab_text
    containing the text for the 'Climate Settings' Menu
mb_settings_tab_text
    containing the text for the 'MB Settings' Menu
general_plot_labels
    labels for plots that are used in more than one plot
climograph_plot_labels
    containing the label only used in the climograph plot
base_climate_timeseries_plot_labels
    containing the labels only used in the timeseries plot
mb_curve_plot_labels
    containing the labels for the mb curve plots (including accumulation and ablation plots)
tab_headings
    containing the headings of the different figure tabs
compare_tab_text
    containing the text only used in the Compare MB tabs
'''

supported_languages = ['en', 'de']

climate_tab_text = {
    # define the heading of the menu
    'heading':
        {
            'en': 'Climate Settings',
            'de': 'Klima Einst.'
        },
    # name for base climate selection
    'base_climate_select_name':
        {
            'en': 'Base Climate',
            'de': 'Basis Klimadaten',
        },
    # include new base climate names, do not forget to include file_suffix (base_climate_file_suffix)
    'base_climate_names':
        {
            'en': ['Artesonraju (Andes, tropical)',           # RGI60-16.02444
                   'Baltoro (Karakoram, continental)',        # RGI60-14.06794
                   'Echaurren Norte (Andes, mediterranean)',  # RGI60-17.13715
                   'Hintereisferner (Alps, continental)',     # RGI60-11.00897
                   'Lewis (Mount Kenya, tropical)',           # RGI60-16.01638
                   'Vestre Torellbreen (Svalbard, polar)',    # RGI60-07.00301
                   'Wolverine (Alaska, maritime)',            # RGI60-01.09162
                  ],
            'de': ['Artesonraju (Anden, tropisch)',
                   'Baltoro (Karakoram, continental)',
                   'Echaurren Norte (Anden, mediterran)',
                   'Hintereisferner (Alpen, continental)',
                   'Lewis (Mount Kenya, tropisch)',
                   'Vestre Torellbreen (Spitzbergen, polar)'
                   'Wolverine (Alaska, seeklima)',
                  ],
        },
    # must be the same order as defined in base_climate_names
    # contains filesuffix of climate data and 
    # ylims (oriented to actual glacier range)
    # hemisphere for hydrological year
    'base_climate_meta_data':
        [['_Art', 3500, 6000, 'sh'],
         ['_Bal', 2100, 8000, 'nh'],
         ['_Ech', 2000, 5000, 'sh'],
         ['_HEF', 1300, 4600, 'nh'],
         ['_Lew', 3500, 5500, 'sh'],
         ['_Ves', 0, 1500, 'nh'],
         ['_Wol', 0, 3000, 'nh']
        ],
    
    'y_start_slider_name':
        {
            'en': 'Start of period',
            'de': 'Start der Periode',
        },

    'y_end_slider_name':
        {
            'en': 'End of period',
            'de': 'Ende der Periode',
        },

    'set_climate_button_name':
        {
            'en': 'Set climate',
            'de': 'Klima festlegen',
        },
}

mb_settings_tab_text = {
    # define the heading of the menu
    'heading':
        {
            'en': 'MB settings',
            'de': 'MB Einst.'
        },
    'mu_slider_name':
        {
            'en': 'Temp. Sensitivity (µ)',
            'de': 'Temp. Sensitivität (µ)',
        },
    'temp_bias_slider_name':
        {
            'en': 'Temperature bias (T_bias)',
            'de': 'Temperatur Bias (T_bias)',
        },
    'temp_grad_slider_name':
        {
            'en': 'Temp. gradient (T_grad)',
            'de': 'Temp. Gradient (T_grad)',
        },
    'prcp_fac_slider_name':
        {
            'en': 'Precipitation factor (Prcp_fac)',
            'de': 'Niederschlags Faktor (Prcp_fac)',
        },
    'temp_melt_slider_name':
        {
            'en': 'T for ice melt (T_melt)',
            'de': 'T für Eisschmelze (T_melt)',
        },
    'temp_solid_slider_name':
        {
            'en': 'T for solid prcp (T_solid)',
            'de': 'T für festen Niederschlag (T_solid)',
        },
    'temp_liquid_slider_name':
        {
            'en': 'T for liquid prcp (T_liquid)',
            'de': 'T für flüssigen Niederschlag (T_liquid)',
        },
    'set_mb_settings_button_name':
        {
            'en': 'Set MB settings',
            'de': 'MB Einst. festlegen',
        },
}

general_plot_labels = {
    'Precipitation':
        {
            'en': 'Precipitation',
            'de': 'Niederschlag',
        },
    'totalPrecipitation':
        {
            'en': 'total Prec.',
            'de': 'totaler Nied.',
        },
    'Temperature':
        {
            'en': 'Temperature',
            'de': 'Temperatur',
        },
    'meanTemperature':
        {
            'en': 'mean Temp.',
            'de': 'mittlere Temp.',
        },
    'Month':
        {
            'en': 'Month',
            'de': 'Monat',
        },
    'Months_long':
        {
            'en': ['October', 'November', 'December', 'January', 'February', 'March',
                   'April', 'May', 'June', 'July', 'August', 'September'],
            'de': ['Oktober', 'November', 'Dezember', 'Januar', 'Februar', 'März',
                   'April', 'Mai', 'Juni', 'Juli', 'August', 'September'],
        },
    'Months_short':
        {
            'en': ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar',
                   'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
            'de': ['Okt', 'Nov', 'Dez', 'Jan', 'Feb', 'Mär',
                   'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep'],
        },
}

climograph_plot_labels = {
    'Height':
        {
            'en': 'Height',
            'de': 'Höhe',
        },
    'Period':
        {
            'en': 'Period',
            'de': 'Periode',
        },
    'to':
        {
            'en': 'to',
            'de': 'bis',
        },
}

base_climate_timeseries_plot_labels = {
    'Year':
        {
            'en': 'Year',
            'de': 'Jahr',
        },
    'Hydro-Year':
        {
            'en': 'Hydro-year',
            'de': 'Hydro-Jahr',
        },
    'Yearly Mean Prcp':
        {
            'en': 'Yearly mean prcp',
            'de': 'Mittl. Jährl. Nieders.',
        },
    'Total Mean Prcp':
        {
            'en': 'Total mean prcp',
            'de': 'Mittl. Totale Nieders.',
        },
    'Yearly Mean Temp':
        {
            'en': 'Yearly mean temp',
            'de': 'Mittl. Jährl. Temp',
        },
    'Total Mean Temp':
        {
            'en': 'Total mean temp',
            'de': 'Mittl. Totale Temp',
        },
    'set_period_buttons_name':
        {
            'en': 'Set period',
            'de': 'Periode setzen',
        },
}

mb_curve_plot_labels = {
    'Height':
        {
            'en': 'Height',
            'de': 'Höhe',
        },
    'kg/m2_and_year':
        {
            'en': 'kg m⁻² year⁻¹',
            'de': 'kg m⁻² Jahr⁻¹',
        },
    'kg/m2_and_month':
        {
            'en': 'kg m⁻² month⁻¹',
            'de': 'kg m⁻² Monat⁻¹',
        },
    'kg/m2_and_year_or_month':
        {
            'en': 'kg m⁻² (year or month)⁻¹',
            'de': 'kg m⁻² (Jahr oder Monat)⁻¹',
        },
    'annual':
        {
            'en': 'Annual',
            'de': 'Jahres',
        },
    'Accumulation':
        {
            'en': 'Accumulation',
            'de': 'Akkumulation',
        },
    'Ablation':
        {
            'en': 'Ablation',
            'de': 'Ablation',
        },
    'Mass-Balance':
        {
            'en': 'Mass-Balance',
            'de': 'Massen-Bilanz',
        },
}

tab_headings = {
    'Mass Balance Model':
        {
            'en': 'Mass Balance',
            'de': 'Massen-Bilanz'
        },
    'Compare Mass Balance Models':
        {
            'en': 'Compare mass balances',
            'de': 'Vergleiche Massen-Bilanz'
        },
    'Current Settings and Climograph':
        {
            'en': 'Current settings and climograph',
            'de': 'Aktuelle Einstellungen und Klimadiagramm'
        },
    'Base Climate Timeseries':
        {
            'en': 'Base climate timeseries',
            'de': 'Basis Klima Zeitreihe'
        },
    'Compare Climographs':
        {
            'en': 'Compare climographs',
            'de': 'Vergleiche Klimadiagramme'
        },
    'Compare MB Settings':
        {
            'en': 'Compare MB settings',
            'de': 'Vergleiche MB Einstellungen'
        }
}

compare_tab_text = {
    'Activate to change MB-Model':
        {
            'en': 'Activate to change MB-Model',
            'de': 'Aktivieren zum ändern von MB-Modell'
        }
}
