/**
 * Frontend Typed Product Specification Matrix Module #13
 */

export interface IProductAttributeDefinition {
  key: string;
  label: string;
  category: string;
  dataType: 'STRING' | 'NUMBER' | 'BOOLEAN';
  isFilterable: boolean;
  unit?: string;
}

export class ProductSpecsMatrixModel1 {
  public static readonly matrixId = 'PSM-13-001';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel2 {
  public static readonly matrixId = 'PSM-13-002';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel3 {
  public static readonly matrixId = 'PSM-13-003';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel4 {
  public static readonly matrixId = 'PSM-13-004';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel5 {
  public static readonly matrixId = 'PSM-13-005';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel6 {
  public static readonly matrixId = 'PSM-13-006';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel7 {
  public static readonly matrixId = 'PSM-13-007';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel8 {
  public static readonly matrixId = 'PSM-13-008';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel9 {
  public static readonly matrixId = 'PSM-13-009';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel10 {
  public static readonly matrixId = 'PSM-13-010';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel11 {
  public static readonly matrixId = 'PSM-13-011';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel12 {
  public static readonly matrixId = 'PSM-13-012';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel13 {
  public static readonly matrixId = 'PSM-13-013';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel14 {
  public static readonly matrixId = 'PSM-13-014';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel15 {
  public static readonly matrixId = 'PSM-13-015';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel16 {
  public static readonly matrixId = 'PSM-13-016';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel17 {
  public static readonly matrixId = 'PSM-13-017';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel18 {
  public static readonly matrixId = 'PSM-13-018';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel19 {
  public static readonly matrixId = 'PSM-13-019';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel20 {
  public static readonly matrixId = 'PSM-13-020';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel21 {
  public static readonly matrixId = 'PSM-13-021';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel22 {
  public static readonly matrixId = 'PSM-13-022';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel23 {
  public static readonly matrixId = 'PSM-13-023';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel24 {
  public static readonly matrixId = 'PSM-13-024';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel25 {
  public static readonly matrixId = 'PSM-13-025';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel26 {
  public static readonly matrixId = 'PSM-13-026';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel27 {
  public static readonly matrixId = 'PSM-13-027';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel28 {
  public static readonly matrixId = 'PSM-13-028';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel29 {
  public static readonly matrixId = 'PSM-13-029';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel30 {
  public static readonly matrixId = 'PSM-13-030';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel31 {
  public static readonly matrixId = 'PSM-13-031';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel32 {
  public static readonly matrixId = 'PSM-13-032';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel33 {
  public static readonly matrixId = 'PSM-13-033';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel34 {
  public static readonly matrixId = 'PSM-13-034';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel35 {
  public static readonly matrixId = 'PSM-13-035';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel36 {
  public static readonly matrixId = 'PSM-13-036';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel37 {
  public static readonly matrixId = 'PSM-13-037';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel38 {
  public static readonly matrixId = 'PSM-13-038';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel39 {
  public static readonly matrixId = 'PSM-13-039';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel40 {
  public static readonly matrixId = 'PSM-13-040';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel41 {
  public static readonly matrixId = 'PSM-13-041';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel42 {
  public static readonly matrixId = 'PSM-13-042';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel43 {
  public static readonly matrixId = 'PSM-13-043';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel44 {
  public static readonly matrixId = 'PSM-13-044';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel45 {
  public static readonly matrixId = 'PSM-13-045';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel46 {
  public static readonly matrixId = 'PSM-13-046';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel47 {
  public static readonly matrixId = 'PSM-13-047';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel48 {
  public static readonly matrixId = 'PSM-13-048';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel49 {
  public static readonly matrixId = 'PSM-13-049';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel50 {
  public static readonly matrixId = 'PSM-13-050';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel51 {
  public static readonly matrixId = 'PSM-13-051';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel52 {
  public static readonly matrixId = 'PSM-13-052';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel53 {
  public static readonly matrixId = 'PSM-13-053';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel54 {
  public static readonly matrixId = 'PSM-13-054';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel55 {
  public static readonly matrixId = 'PSM-13-055';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel56 {
  public static readonly matrixId = 'PSM-13-056';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel57 {
  public static readonly matrixId = 'PSM-13-057';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel58 {
  public static readonly matrixId = 'PSM-13-058';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel59 {
  public static readonly matrixId = 'PSM-13-059';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel60 {
  public static readonly matrixId = 'PSM-13-060';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel61 {
  public static readonly matrixId = 'PSM-13-061';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel62 {
  public static readonly matrixId = 'PSM-13-062';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel63 {
  public static readonly matrixId = 'PSM-13-063';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel64 {
  public static readonly matrixId = 'PSM-13-064';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel65 {
  public static readonly matrixId = 'PSM-13-065';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel66 {
  public static readonly matrixId = 'PSM-13-066';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel67 {
  public static readonly matrixId = 'PSM-13-067';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel68 {
  public static readonly matrixId = 'PSM-13-068';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel69 {
  public static readonly matrixId = 'PSM-13-069';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel70 {
  public static readonly matrixId = 'PSM-13-070';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel71 {
  public static readonly matrixId = 'PSM-13-071';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel72 {
  public static readonly matrixId = 'PSM-13-072';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel73 {
  public static readonly matrixId = 'PSM-13-073';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel74 {
  public static readonly matrixId = 'PSM-13-074';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel75 {
  public static readonly matrixId = 'PSM-13-075';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel76 {
  public static readonly matrixId = 'PSM-13-076';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel77 {
  public static readonly matrixId = 'PSM-13-077';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel78 {
  public static readonly matrixId = 'PSM-13-078';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel79 {
  public static readonly matrixId = 'PSM-13-079';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel80 {
  public static readonly matrixId = 'PSM-13-080';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel81 {
  public static readonly matrixId = 'PSM-13-081';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel82 {
  public static readonly matrixId = 'PSM-13-082';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel83 {
  public static readonly matrixId = 'PSM-13-083';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel84 {
  public static readonly matrixId = 'PSM-13-084';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel85 {
  public static readonly matrixId = 'PSM-13-085';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel86 {
  public static readonly matrixId = 'PSM-13-086';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel87 {
  public static readonly matrixId = 'PSM-13-087';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel88 {
  public static readonly matrixId = 'PSM-13-088';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel89 {
  public static readonly matrixId = 'PSM-13-089';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel90 {
  public static readonly matrixId = 'PSM-13-090';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel91 {
  public static readonly matrixId = 'PSM-13-091';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel92 {
  public static readonly matrixId = 'PSM-13-092';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel93 {
  public static readonly matrixId = 'PSM-13-093';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel94 {
  public static readonly matrixId = 'PSM-13-094';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel95 {
  public static readonly matrixId = 'PSM-13-095';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel96 {
  public static readonly matrixId = 'PSM-13-096';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel97 {
  public static readonly matrixId = 'PSM-13-097';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel98 {
  public static readonly matrixId = 'PSM-13-098';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel99 {
  public static readonly matrixId = 'PSM-13-099';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel100 {
  public static readonly matrixId = 'PSM-13-100';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel101 {
  public static readonly matrixId = 'PSM-13-101';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel102 {
  public static readonly matrixId = 'PSM-13-102';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel103 {
  public static readonly matrixId = 'PSM-13-103';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel104 {
  public static readonly matrixId = 'PSM-13-104';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel105 {
  public static readonly matrixId = 'PSM-13-105';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel106 {
  public static readonly matrixId = 'PSM-13-106';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel107 {
  public static readonly matrixId = 'PSM-13-107';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel108 {
  public static readonly matrixId = 'PSM-13-108';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel109 {
  public static readonly matrixId = 'PSM-13-109';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel110 {
  public static readonly matrixId = 'PSM-13-110';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel111 {
  public static readonly matrixId = 'PSM-13-111';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel112 {
  public static readonly matrixId = 'PSM-13-112';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel113 {
  public static readonly matrixId = 'PSM-13-113';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel114 {
  public static readonly matrixId = 'PSM-13-114';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel115 {
  public static readonly matrixId = 'PSM-13-115';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel116 {
  public static readonly matrixId = 'PSM-13-116';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel117 {
  public static readonly matrixId = 'PSM-13-117';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel118 {
  public static readonly matrixId = 'PSM-13-118';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel119 {
  public static readonly matrixId = 'PSM-13-119';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

export class ProductSpecsMatrixModel120 {
  public static readonly matrixId = 'PSM-13-120';

  public static getAttributes(): IProductAttributeDefinition[] {
    return [
      { key: 'processor', label: 'Processor / Chipset', category: 'Performance', dataType: 'STRING', isFilterable: true },
      { key: 'ram_capacity_gb', label: 'RAM Capacity', category: 'Memory', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'storage_capacity_gb', label: 'Internal Storage', category: 'Storage', dataType: 'NUMBER', isFilterable: true, unit: 'GB' },
      { key: 'display_refresh_rate', label: 'Screen Refresh Rate', category: 'Display', dataType: 'NUMBER', isFilterable: true, unit: 'Hz' },
      { key: 'battery_capacity_mah', label: 'Battery Capacity', category: 'Battery', dataType: 'NUMBER', isFilterable: true, unit: 'mAh' },
      { key: 'has_5g_connectivity', label: '5G Connectivity Support', category: 'Network', dataType: 'BOOLEAN', isFilterable: true },
      { key: 'warranty_duration_months', label: 'Standard Warranty', category: 'Warranty', dataType: 'NUMBER', isFilterable: false, unit: 'Months' }
    ];
  }

  public static formatDisplayValue(key: string, value: any): string {
    if (typeof value === 'boolean') return value ? 'Supported' : 'Not Supported';
    if (key === 'ram_capacity_gb' || key === 'storage_capacity_gb') return `${value} GB`;
    if (key === 'display_refresh_rate') return `${value} Hz`;
    if (key === 'battery_capacity_mah') return `${value} mAh`;
    return String(value);
  }
}

