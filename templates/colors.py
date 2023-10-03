txt = '''
		// Style Tab || {section_name_u}
		$this->start_controls_section(
			'{theme_name}_{section_name}_style',
			[
				'label' => esc_html__( '{section_name_u} Colors', '{lang_domain}' ),
				'tab' => \Elementor\Controls_Manager::TAB_STYLE,
			]
		);

		// {section_name_u} Menu Heading
		$this->add_control(
			'{theme_name}_{section_name}_head',[
			'label' => esc_html( 'Text Color', '{lang_domain}'),
			'type'	=>  \Elementor\Controls_Manager::HEADING,
		]);

		// {section_name_u} Text Color
		$this->add_control(
			'{theme_name}_{section_name}_text_color',
			[
				'label' => esc_html__( 'Color', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{{{WRAPPER}}}} .{class_name}' => 'color: {{{{VALUE}}}};',
				],
			]
		);

		// {section_name_u} Type Color
		$this -> add_group_control(
			\Elementor\Group_Control_Typography::get_type(),
			[
				'name'		=> '{theme_name}_{section_name}_type',
				'selector'	=> '{{{{WRAPPER}}}} .{class_name}',
				
			]
		);

		$this->end_controls_section();

'''
