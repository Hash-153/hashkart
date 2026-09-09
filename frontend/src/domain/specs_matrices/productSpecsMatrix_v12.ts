/**
 * Frontend Typed Product Specification Matrix Module #12
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
  public static readonly matrixId = 'PSM-12-001';

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
  public static readonly matrixId = 'PSM-12-002';

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
  public static readonly matrixId = 'PSM-12-003';

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
  public static readonly matrixId = 'PSM-12-004';

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
  public static readonly matrixId = 'PSM-12-005';

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
  public static readonly matrixId = 'PSM-12-006';

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
  public static readonly matrixId = 'PSM-12-007';

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
  public static readonly matrixId = 'PSM-12-008';

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
  public static readonly matrixId = 'PSM-12-009';

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
  public static readonly matrixId = 'PSM-12-010';

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
  public static readonly matrixId = 'PSM-12-011';

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
  public static readonly matrixId = 'PSM-12-012';

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
  public static readonly matrixId = 'PSM-12-013';

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
  public static readonly matrixId = 'PSM-12-014';

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
  public static readonly matrixId = 'PSM-12-015';

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
  public static readonly matrixId = 'PSM-12-016';

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
  public static readonly matrixId = 'PSM-12-017';

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
  public static readonly matrixId = 'PSM-12-018';

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
  public static readonly matrixId = 'PSM-12-019';

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
  public static readonly matrixId = 'PSM-12-020';

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
  public static readonly matrixId = 'PSM-12-021';

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
  public static readonly matrixId = 'PSM-12-022';

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
  public static readonly matrixId = 'PSM-12-023';

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
  public static readonly matrixId = 'PSM-12-024';

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
  public static readonly matrixId = 'PSM-12-025';

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
  public static readonly matrixId = 'PSM-12-026';

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
  public static readonly matrixId = 'PSM-12-027';

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
  public static readonly matrixId = 'PSM-12-028';

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
  public static readonly matrixId = 'PSM-12-029';

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
  public static readonly matrixId = 'PSM-12-030';

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
  public static readonly matrixId = 'PSM-12-031';

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
  public static readonly matrixId = 'PSM-12-032';

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
  public static readonly matrixId = 'PSM-12-033';

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
  public static readonly matrixId = 'PSM-12-034';

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
  public static readonly matrixId = 'PSM-12-035';

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
  public static readonly matrixId = 'PSM-12-036';

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
  public static readonly matrixId = 'PSM-12-037';

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
  public static readonly matrixId = 'PSM-12-038';

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
  public static readonly matrixId = 'PSM-12-039';

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
  public static readonly matrixId = 'PSM-12-040';

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
  public static readonly matrixId = 'PSM-12-041';

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
  public static readonly matrixId = 'PSM-12-042';

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
  public static readonly matrixId = 'PSM-12-043';

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
  public static readonly matrixId = 'PSM-12-044';

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
  public static readonly matrixId = 'PSM-12-045';

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
  public static readonly matrixId = 'PSM-12-046';

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
  public static readonly matrixId = 'PSM-12-047';

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
  public static readonly matrixId = 'PSM-12-048';

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
  public static readonly matrixId = 'PSM-12-049';

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
  public static readonly matrixId = 'PSM-12-050';

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
  public static readonly matrixId = 'PSM-12-051';

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
  public static readonly matrixId = 'PSM-12-052';

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
  public static readonly matrixId = 'PSM-12-053';

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
  public static readonly matrixId = 'PSM-12-054';

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
  public static readonly matrixId = 'PSM-12-055';

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
  public static readonly matrixId = 'PSM-12-056';

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
  public static readonly matrixId = 'PSM-12-057';

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
  public static readonly matrixId = 'PSM-12-058';

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
  public static readonly matrixId = 'PSM-12-059';

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
  public static readonly matrixId = 'PSM-12-060';

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
  public static readonly matrixId = 'PSM-12-061';

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
  public static readonly matrixId = 'PSM-12-062';

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
  public static readonly matrixId = 'PSM-12-063';

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
  public static readonly matrixId = 'PSM-12-064';

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
  public static readonly matrixId = 'PSM-12-065';

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
  public static readonly matrixId = 'PSM-12-066';

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
  public static readonly matrixId = 'PSM-12-067';

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
  public static readonly matrixId = 'PSM-12-068';

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
  public static readonly matrixId = 'PSM-12-069';

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
  public static readonly matrixId = 'PSM-12-070';

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
  public static readonly matrixId = 'PSM-12-071';

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
  public static readonly matrixId = 'PSM-12-072';

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
  public static readonly matrixId = 'PSM-12-073';

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
  public static readonly matrixId = 'PSM-12-074';

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
  public static readonly matrixId = 'PSM-12-075';

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
  public static readonly matrixId = 'PSM-12-076';

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
  public static readonly matrixId = 'PSM-12-077';

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
  public static readonly matrixId = 'PSM-12-078';

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
  public static readonly matrixId = 'PSM-12-079';

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
  public static readonly matrixId = 'PSM-12-080';

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
  public static readonly matrixId = 'PSM-12-081';

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
  public static readonly matrixId = 'PSM-12-082';

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
  public static readonly matrixId = 'PSM-12-083';

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
  public static readonly matrixId = 'PSM-12-084';

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
  public static readonly matrixId = 'PSM-12-085';

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
  public static readonly matrixId = 'PSM-12-086';

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
  public static readonly matrixId = 'PSM-12-087';

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
  public static readonly matrixId = 'PSM-12-088';

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
  public static readonly matrixId = 'PSM-12-089';

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
  public static readonly matrixId = 'PSM-12-090';

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
  public static readonly matrixId = 'PSM-12-091';

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
  public static readonly matrixId = 'PSM-12-092';

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
  public static readonly matrixId = 'PSM-12-093';

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
  public static readonly matrixId = 'PSM-12-094';

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
  public static readonly matrixId = 'PSM-12-095';

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
  public static readonly matrixId = 'PSM-12-096';

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
  public static readonly matrixId = 'PSM-12-097';

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
  public static readonly matrixId = 'PSM-12-098';

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
  public static readonly matrixId = 'PSM-12-099';

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
  public static readonly matrixId = 'PSM-12-100';

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
  public static readonly matrixId = 'PSM-12-101';

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
  public static readonly matrixId = 'PSM-12-102';

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
  public static readonly matrixId = 'PSM-12-103';

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
  public static readonly matrixId = 'PSM-12-104';

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
  public static readonly matrixId = 'PSM-12-105';

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
  public static readonly matrixId = 'PSM-12-106';

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
  public static readonly matrixId = 'PSM-12-107';

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
  public static readonly matrixId = 'PSM-12-108';

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
  public static readonly matrixId = 'PSM-12-109';

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
  public static readonly matrixId = 'PSM-12-110';

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
  public static readonly matrixId = 'PSM-12-111';

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
  public static readonly matrixId = 'PSM-12-112';

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
  public static readonly matrixId = 'PSM-12-113';

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
  public static readonly matrixId = 'PSM-12-114';

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
  public static readonly matrixId = 'PSM-12-115';

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
  public static readonly matrixId = 'PSM-12-116';

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
  public static readonly matrixId = 'PSM-12-117';

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
  public static readonly matrixId = 'PSM-12-118';

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
  public static readonly matrixId = 'PSM-12-119';

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
  public static readonly matrixId = 'PSM-12-120';

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

