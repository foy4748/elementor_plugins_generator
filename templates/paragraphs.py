txt = '''
        // Content Control
		$this->add_control(
			'{theme_name}_{section_name}_content',
			[
				'label' => esc_html__( '{section_name_u} Content', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::WYSIWYG,
				'default' => esc_html__('{section_content_default}' , '{lang_domain}'),
				'placeholder' => __( 'Your Conent', '{lang_domain}' ),
			]
		);


		$this->end_controls_section();
'''
