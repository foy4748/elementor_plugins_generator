txt = '''
		$this->start_controls_section(
			'{theme_name}_{section_name}_headings_widget',
			[
				'label' => esc_html__( '{section_name_u} Headings', '{lang_domain}' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

		// {section_name_u} Title Control
		$this->add_control(
			'{theme_name}_{section_name}_title',
			[
				'label' => esc_html__( '{section_name_u} Title', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::WYSIWYG,
				'default' => esc_html__('{section_title_default}' , '{lang_domain}'),
				'placeholder' => __( 'Your Title', '{lang_domain}' ),
			]
		);

		// {section_name_u} Sub Title Control
		$this->add_control(
			'{theme_name}_{section_name}_subtitle',
			[
				'label' => esc_html__( '{section_name_u} SubTitle', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::WYSIWYG,
				'default' => esc_html__('{section_subtitle_default}' , '{lang_domain}'),
				'placeholder' => __( 'Your SubTitle', '{lang_domain}' ),
			]
		);

		$this->end_controls_section();
'''
