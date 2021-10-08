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
            'en': ['Austre Broeggerbreen (Svalbard, polar)',  # RGI60-07.00504
                   'Baltoro (Karakoram, continental)',        # RGI60-14.06794
                   'Echaurren Norte (Andes, mediterranean)',  # RGI60-17.13715
                   'Hintereisferner (Alps, continental)',     # RGI60-11.00897
                   'Lewis (Mount Kenya, tropical)',           # RGI60-16.01638
                   'Wolverine (Alaska, maritime)',            # RGI60-01.09162
                  ],			
            'de': ['Austre Broeggerbreen (Spitzbergen, polar)',
                   'Baltoro (Karakoram, continental)',
                   'Echaurren Norte (Anden, mediterran)',
                   'Hintereisferner (Alpen, continental)',
                   'Lewis (Mount Kenya, tropisch)',
                   'Wolverine (Alaska, seeklima)',
                  ],
        },
    # must be the same order as defined in base_climate_names
    'base_climate_file_suffix':
        ['_Aus',
         '_Bal',
         '_Ech',
         '_HEF',
         '_Lew',
         '_Wol',
        ],
    
    'y_start_slider_name':
        {
            'en': 'Start of Period',
            'de': 'Start der Periode',
        },

    'y_end_slider_name':
        {
            'en': 'End of Preiod',
            'de': 'Ende der Periode',
        },

    'set_climate_button_name':
        {
            'en': 'Set Climate',
            'de': 'Klima festlegen',
        },
}

mb_settings_tab_text = {
    # define the heading of the menu
    'heading':
        {
            'en': 'MB Settings',
            'de': 'MB Einst.'
        },
    'mu_slider_name':
        {
            'en': 'Sensitivity Parameter (µ)',
            'de': 'Sensitivitäts Parameter (µ)',
        },
    'temp_bias_slider_name':
        {
            'en': 'Temperature Bias (T_bias)',
            'de': 'Temperatur Bias (T_bias)',
        },
    'temp_grad_slider_name':
        {
            'en': 'Temp. Gradient (T_grad)',
            'de': 'Temp. Gradient (T_grad)',
        },
    'prcp_fac_slider_name':
        {
            'en': 'Precipitation Factor (Prcp_fac)',
            'de': 'Niederschlags Faktor (Prcp_fac)',
        },
    'temp_melt_slider_name':
        {
            'en': 'T for ice melt (T_melt)',
            'de': 'T für Eisschmelze (T_melt)',
        },
    'temp_solid_slider_name':
        {
            'en': 'T for solid Prcp only (T_solid)',
            'de': 'T für festen Niederschlag (T_solid)',
        },
    'temp_liquid_slider_name':
        {
            'en': 'T for liquid Prcp only (T_liquid)',
            'de': 'T für flüssigen Niederschlag (T_liquid)',
        },
    'set_mb_settings_button_name':
        {
            'en': 'Set MB Settings',
            'de': 'MB Einst. festlegen',
        },
}

general_plot_labels = {
    'Precipitation':
        {
            'en': 'Precipitation',
            'de': 'Niederschlag',
        },
    'Temperature':
        {
            'en': 'Temperature',
            'de': 'Temperatur',
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
            'en': 'Hydro-Year',
            'de': 'Hydro-Jahr',
        },
    'Yearly Mean Prcp':
        {
            'en': 'Yearly Mean Prcp',
            'de': 'Mittl. Jährl. Nieders.',
        },
    'Total Mean Prcp':
        {
            'en': 'Total Mean Prcp',
            'de': 'Mittl. Totale Nieders.',
        },
    'Yearly Mean Temp':
        {
            'en': 'Yearly Mean Temp',
            'de': 'Mittl. Jährl. Temp',
        },
    'Total Mean Temp':
        {
            'en': 'Total Mean Temp',
            'de': 'Mittl. Totale Temp',
        },
    'set_period_buttons_name':
        {
            'en': 'Set Period',
            'de': 'Periode setzen',
        },
}

mb_curve_plot_labels = {
    'Height':
        {
            'en': 'Height',
            'de': 'Höhe',
        },
    'm/year':
        {
            'en': 'm/Year',
            'de': 'm/Jahr',
        },
    'm/month':
        {
            'en': 'm/Month',
            'de': 'm/Monat',
        },
    'm/year or month':
        {
            'en': 'm/Year or Month',
            'de': 'm/Jahr oder Monat',
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
            'en': 'Mass Balance Model',
            'de': 'Massen-Bilanz Modell'
        },
    'Compare Mass Balance Models':
        {
            'en': 'Compare Mass Balance Models',
            'de': 'Vergleiche Massen-Bilanz Modelle'
        },
    'Current Settings and Climograph':
        {
            'en': 'Current Settings and Climograph',
            'de': 'Aktuelle Einstellungen und Klimadiagramm'
        },
    'Base Climate Timeseries':
        {
            'en': 'Base Climate Timeseries',
            'de': 'Basis Klima Zeitreihe'
        },
    'Compare Climographs':
        {
            'en': 'Compare Climographs',
            'de': 'Vergleiche Klimadiagramme'
        },
    'Compare MB Settings':
        {
            'en': 'Compare MB Settings',
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
