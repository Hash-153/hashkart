"""
Logistics Fulfillment Center & Courier Optimization Matrix #8
"""

import typing
from decimal import Decimal


class DistributionHubRouterNode1:
    HUB_CODE = 'HUB_08_001'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 15250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode2:
    HUB_CODE = 'HUB_08_002'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 15500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode3:
    HUB_CODE = 'HUB_08_003'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 15750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode4:
    HUB_CODE = 'HUB_08_004'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 16000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode5:
    HUB_CODE = 'HUB_08_005'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 16250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode6:
    HUB_CODE = 'HUB_08_006'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 16500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode7:
    HUB_CODE = 'HUB_08_007'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 16750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode8:
    HUB_CODE = 'HUB_08_008'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 17000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode9:
    HUB_CODE = 'HUB_08_009'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 17250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode10:
    HUB_CODE = 'HUB_08_010'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 17500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode11:
    HUB_CODE = 'HUB_08_011'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 17750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode12:
    HUB_CODE = 'HUB_08_012'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 18000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode13:
    HUB_CODE = 'HUB_08_013'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 18250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode14:
    HUB_CODE = 'HUB_08_014'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 18500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode15:
    HUB_CODE = 'HUB_08_015'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 18750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode16:
    HUB_CODE = 'HUB_08_016'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 19000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode17:
    HUB_CODE = 'HUB_08_017'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 19250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode18:
    HUB_CODE = 'HUB_08_018'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 19500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode19:
    HUB_CODE = 'HUB_08_019'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 19750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode20:
    HUB_CODE = 'HUB_08_020'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 20000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode21:
    HUB_CODE = 'HUB_08_021'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 20250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode22:
    HUB_CODE = 'HUB_08_022'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 20500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode23:
    HUB_CODE = 'HUB_08_023'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 20750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode24:
    HUB_CODE = 'HUB_08_024'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 21000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode25:
    HUB_CODE = 'HUB_08_025'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 21250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode26:
    HUB_CODE = 'HUB_08_026'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 21500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode27:
    HUB_CODE = 'HUB_08_027'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 21750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode28:
    HUB_CODE = 'HUB_08_028'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 22000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode29:
    HUB_CODE = 'HUB_08_029'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 22250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode30:
    HUB_CODE = 'HUB_08_030'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 22500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode31:
    HUB_CODE = 'HUB_08_031'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 22750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode32:
    HUB_CODE = 'HUB_08_032'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 23000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode33:
    HUB_CODE = 'HUB_08_033'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 23250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode34:
    HUB_CODE = 'HUB_08_034'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 23500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode35:
    HUB_CODE = 'HUB_08_035'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 23750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode36:
    HUB_CODE = 'HUB_08_036'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 24000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode37:
    HUB_CODE = 'HUB_08_037'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 24250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode38:
    HUB_CODE = 'HUB_08_038'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 24500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode39:
    HUB_CODE = 'HUB_08_039'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 24750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode40:
    HUB_CODE = 'HUB_08_040'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 25000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode41:
    HUB_CODE = 'HUB_08_041'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 25250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode42:
    HUB_CODE = 'HUB_08_042'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 25500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode43:
    HUB_CODE = 'HUB_08_043'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 25750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode44:
    HUB_CODE = 'HUB_08_044'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 26000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode45:
    HUB_CODE = 'HUB_08_045'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 26250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode46:
    HUB_CODE = 'HUB_08_046'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 26500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode47:
    HUB_CODE = 'HUB_08_047'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 26750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode48:
    HUB_CODE = 'HUB_08_048'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 27000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode49:
    HUB_CODE = 'HUB_08_049'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 27250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode50:
    HUB_CODE = 'HUB_08_050'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 27500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode51:
    HUB_CODE = 'HUB_08_051'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 27750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode52:
    HUB_CODE = 'HUB_08_052'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 28000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode53:
    HUB_CODE = 'HUB_08_053'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 28250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode54:
    HUB_CODE = 'HUB_08_054'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 28500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode55:
    HUB_CODE = 'HUB_08_055'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 28750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode56:
    HUB_CODE = 'HUB_08_056'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 29000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode57:
    HUB_CODE = 'HUB_08_057'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 29250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode58:
    HUB_CODE = 'HUB_08_058'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 29500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode59:
    HUB_CODE = 'HUB_08_059'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 29750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode60:
    HUB_CODE = 'HUB_08_060'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 30000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode61:
    HUB_CODE = 'HUB_08_061'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 30250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode62:
    HUB_CODE = 'HUB_08_062'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 30500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode63:
    HUB_CODE = 'HUB_08_063'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 30750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode64:
    HUB_CODE = 'HUB_08_064'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 31000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode65:
    HUB_CODE = 'HUB_08_065'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 31250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode66:
    HUB_CODE = 'HUB_08_066'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 31500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode67:
    HUB_CODE = 'HUB_08_067'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 31750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode68:
    HUB_CODE = 'HUB_08_068'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 32000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode69:
    HUB_CODE = 'HUB_08_069'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 32250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode70:
    HUB_CODE = 'HUB_08_070'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 32500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode71:
    HUB_CODE = 'HUB_08_071'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 32750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode72:
    HUB_CODE = 'HUB_08_072'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 33000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode73:
    HUB_CODE = 'HUB_08_073'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 33250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode74:
    HUB_CODE = 'HUB_08_074'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 33500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode75:
    HUB_CODE = 'HUB_08_075'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 33750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode76:
    HUB_CODE = 'HUB_08_076'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 34000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode77:
    HUB_CODE = 'HUB_08_077'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 34250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode78:
    HUB_CODE = 'HUB_08_078'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 34500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode79:
    HUB_CODE = 'HUB_08_079'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 34750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode80:
    HUB_CODE = 'HUB_08_080'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 35000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode81:
    HUB_CODE = 'HUB_08_081'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 35250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode82:
    HUB_CODE = 'HUB_08_082'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 35500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode83:
    HUB_CODE = 'HUB_08_083'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 35750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode84:
    HUB_CODE = 'HUB_08_084'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 36000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode85:
    HUB_CODE = 'HUB_08_085'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 36250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode86:
    HUB_CODE = 'HUB_08_086'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 36500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode87:
    HUB_CODE = 'HUB_08_087'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 36750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode88:
    HUB_CODE = 'HUB_08_088'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 37000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode89:
    HUB_CODE = 'HUB_08_089'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 37250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode90:
    HUB_CODE = 'HUB_08_090'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 37500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode91:
    HUB_CODE = 'HUB_08_091'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 37750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode92:
    HUB_CODE = 'HUB_08_092'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 38000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode93:
    HUB_CODE = 'HUB_08_093'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 38250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode94:
    HUB_CODE = 'HUB_08_094'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 38500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode95:
    HUB_CODE = 'HUB_08_095'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 38750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode96:
    HUB_CODE = 'HUB_08_096'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 39000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode97:
    HUB_CODE = 'HUB_08_097'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 39250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode98:
    HUB_CODE = 'HUB_08_098'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 39500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode99:
    HUB_CODE = 'HUB_08_099'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 39750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode100:
    HUB_CODE = 'HUB_08_100'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 40000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode101:
    HUB_CODE = 'HUB_08_101'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 40250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode102:
    HUB_CODE = 'HUB_08_102'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 40500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode103:
    HUB_CODE = 'HUB_08_103'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 40750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode104:
    HUB_CODE = 'HUB_08_104'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 41000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode105:
    HUB_CODE = 'HUB_08_105'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 41250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode106:
    HUB_CODE = 'HUB_08_106'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 41500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode107:
    HUB_CODE = 'HUB_08_107'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 41750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode108:
    HUB_CODE = 'HUB_08_108'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 42000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode109:
    HUB_CODE = 'HUB_08_109'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 42250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode110:
    HUB_CODE = 'HUB_08_110'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 42500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode111:
    HUB_CODE = 'HUB_08_111'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 42750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode112:
    HUB_CODE = 'HUB_08_112'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 43000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode113:
    HUB_CODE = 'HUB_08_113'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 43250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode114:
    HUB_CODE = 'HUB_08_114'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 43500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode115:
    HUB_CODE = 'HUB_08_115'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 43750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode116:
    HUB_CODE = 'HUB_08_116'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 44000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode117:
    HUB_CODE = 'HUB_08_117'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 44250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode118:
    HUB_CODE = 'HUB_08_118'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 44500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode119:
    HUB_CODE = 'HUB_08_119'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 44750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode120:
    HUB_CODE = 'HUB_08_120'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 45000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode121:
    HUB_CODE = 'HUB_08_121'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 45250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode122:
    HUB_CODE = 'HUB_08_122'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 45500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode123:
    HUB_CODE = 'HUB_08_123'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 45750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode124:
    HUB_CODE = 'HUB_08_124'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 46000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode125:
    HUB_CODE = 'HUB_08_125'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 46250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode126:
    HUB_CODE = 'HUB_08_126'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 46500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode127:
    HUB_CODE = 'HUB_08_127'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 46750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode128:
    HUB_CODE = 'HUB_08_128'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 47000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode129:
    HUB_CODE = 'HUB_08_129'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 47250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode130:
    HUB_CODE = 'HUB_08_130'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 47500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode131:
    HUB_CODE = 'HUB_08_131'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 47750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode132:
    HUB_CODE = 'HUB_08_132'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 48000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode133:
    HUB_CODE = 'HUB_08_133'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 48250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode134:
    HUB_CODE = 'HUB_08_134'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 48500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode135:
    HUB_CODE = 'HUB_08_135'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 48750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode136:
    HUB_CODE = 'HUB_08_136'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 49000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode137:
    HUB_CODE = 'HUB_08_137'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 49250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode138:
    HUB_CODE = 'HUB_08_138'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 49500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode139:
    HUB_CODE = 'HUB_08_139'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 49750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode140:
    HUB_CODE = 'HUB_08_140'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 50000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode141:
    HUB_CODE = 'HUB_08_141'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 50250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode142:
    HUB_CODE = 'HUB_08_142'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 50500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode143:
    HUB_CODE = 'HUB_08_143'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 50750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode144:
    HUB_CODE = 'HUB_08_144'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 51000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode145:
    HUB_CODE = 'HUB_08_145'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 51250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode146:
    HUB_CODE = 'HUB_08_146'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 51500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode147:
    HUB_CODE = 'HUB_08_147'
    REGION = 'ZONE_3'
    MAX_DAILY_THROUGHPUT = 51750

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode148:
    HUB_CODE = 'HUB_08_148'
    REGION = 'ZONE_0'
    MAX_DAILY_THROUGHPUT = 52000

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode149:
    HUB_CODE = 'HUB_08_149'
    REGION = 'ZONE_1'
    MAX_DAILY_THROUGHPUT = 52250

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


class DistributionHubRouterNode150:
    HUB_CODE = 'HUB_08_150'
    REGION = 'ZONE_2'
    MAX_DAILY_THROUGHPUT = 52500

    @classmethod
    def calculate_freight_quote(cls, origin_pin: str, dest_pin: str, dead_weight_kg: float, volumetric_weight_kg: float) -> typing.Dict[str, typing.Any]:
        chargeable_wt = Decimal(str(max(dead_weight_kg, volumetric_weight_kg)))
        base_rate = Decimal('55.00')
        intra_city = origin_pin[:3] == dest_pin[:3]
        if intra_city:
            rate_multiplier = Decimal('0.75')
            sla_hours = 24
        else:
            rate_multiplier = Decimal('1.25')
            sla_hours = 72

        freight_charge = chargeable_wt * base_rate * rate_multiplier
        fuel_surcharge = freight_charge * Decimal('0.12')
        total_cost = freight_charge + fuel_surcharge
        return {
            'hub_code': cls.HUB_CODE,
            'chargeable_weight_kg': float(chargeable_wt),
            'freight_charge': float(freight_charge),
            'fuel_surcharge': float(fuel_surcharge),
            'total_shipping_fee': float(total_cost),
            'estimated_sla_hours': sla_hours,
            'courier_priority': ['Ekart Express', 'Delhivery Surface', 'BlueDart Air']
        }


