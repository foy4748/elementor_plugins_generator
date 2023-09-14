txt = '''
		// Image Control ------------------------------
		$this->start_controls_section(
			'{theme_name}_{section_name}_image_widget',
			[
				'label' => esc_html__( '{section_name_u} Image', '{lang_domain}' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

		$this->add_control(
			'{theme_name}_{section_name}_image',
			[
				'label' => esc_html__( 'Choose an Image', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'default' => [
					'url' => {theme_img_dir_variable}.'{img_filename}',
				],
			]
		);

		$this->end_controls_section();

'''
