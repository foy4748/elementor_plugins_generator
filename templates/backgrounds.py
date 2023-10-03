txt = '''
		//{section_name_u} Background
		$this->add_control(
			'{section_name}_bg_head',[
			'label' => esc_html( '{section_name_u} Background', '{lang_domain}'),
			'type'	=>  Controls_Manager::HEADING,
		]);

		$this->add_group_control(
			Group_Control_Background::get_type(),
			[
				'name' => '{section_name}__bg',
				'types' => [ 'classic', 'gradient', 'video' ],
				'selector' => '{{{{WRAPPER}}}} .{class_name}',
			]
		);

		$this->end_controls_section();
'''
