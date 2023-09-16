txt = '''
		$this->start_controls_section(
			'{theme_name}_{section_name}_items',
			[
				'label' => esc_html__( '{theme_name} {section_name_u}', '{lang_domain}' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);
		${theme_name}_{section_name}_item = new \Elementor\Repeater();
		${theme_name}_{section_name}_item->add_control(
			'{theme_name}_{section_name}_item_title',
			[
				'label' => esc_html__( '{section_name_u} Title', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => esc_html__("{repeater_item_title_default}", '{lang_domain}'),
			]
		);
		${theme_name}_{section_name}_item->add_control(
			'{theme_name}_{section_name}_item_icon',
			[
				'label' => esc_html__( '{section_name_u} Icon/Img', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::MEDIA,
				'default' => [
					'url' =>  {theme_img_dir_variable}.'{repeater_item_icon_default}'
				],
			]
		);
		$this->add_control(
			'{theme_name}_{section_name}_item_repeater',
			[
				'label' => esc_html__( 'Add A Icon', '{lang_domain}' ),
				'type' => \Elementor\Controls_Manager::REPEATER,
				'fields' => ${theme_name}_{section_name}_item->get_controls(),
				'default' => [
						'{theme_name}_{section_name}_item_title' =>  esc_html__("{repeater_item_title_default}", '{lang_domain}'),
				],
				'title_field' => '{{{{{{ {theme_name}_{section_name}_item_title }}}}}}',
			]
		);
		$this->end_controls_section();

'''
