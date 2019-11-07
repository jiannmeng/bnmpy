import pytest
import responses

from bnmpy import BASE_URL, Bnmpy

null = None


@pytest.fixture
def mock_base_rate():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as r:
        r.add(
            responses.GET,
            BASE_URL + "base-rate",
            json={
                "data": [
                    {
                        "bank_code": "BKKBMYKL",
                        "bank_name": "Bangkok Bank Berhad",
                        "base_rate": 4.47,
                        "base_lending_rate": 7.14,
                        "indicative_eff_lending_rate": 5.67,
                    },
                    {
                        "bank_code": "CIBBMYKL",
                        "bank_name": "CIMB Bank Berhad",
                        "base_rate": 4,
                        "base_lending_rate": 6.85,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "CITIMYKL",
                        "bank_name": "Citibank Berhad",
                        "base_rate": 3.65,
                        "base_lending_rate": 6.8,
                        "indicative_eff_lending_rate": 4.45,
                    },
                    {
                        "bank_code": "HLBBMYKL",
                        "bank_name": "Hong Leong Bank Malaysia Berhad",
                        "base_rate": 3.88,
                        "base_lending_rate": 6.89,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "HBMBMYKL",
                        "bank_name": "HSBC Bank Malaysia Berhad",
                        "base_rate": 3.64,
                        "base_lending_rate": 6.74,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "ICBKMYKL",
                        "bank_name": "Industrial and Commercial Bank of China (Malaysia) Berhad",
                        "base_rate": 3.77,
                        "base_lending_rate": 6.7,
                        "indicative_eff_lending_rate": 4.6,
                    },
                    {
                        "bank_code": "MBBEMYKL",
                        "bank_name": "Malayan Banking Berhad",
                        "base_rate": 3,
                        "base_lending_rate": 6.65,
                        "indicative_eff_lending_rate": 4.35,
                    },
                    {
                        "bank_code": "OCBCMYKL",
                        "bank_name": "OCBC Bank (Malaysia) Berhad",
                        "base_rate": 3.83,
                        "base_lending_rate": 6.76,
                        "indicative_eff_lending_rate": 4.7,
                    },
                    {
                        "bank_code": "PBBEMYKL",
                        "bank_name": "Public Bank Berhad",
                        "base_rate": 3.52,
                        "base_lending_rate": 6.72,
                        "indicative_eff_lending_rate": 4.35,
                    },
                    {
                        "bank_code": "RHBBMYKL",
                        "bank_name": "RHB Bank Berhad",
                        "base_rate": 3.75,
                        "base_lending_rate": 6.7,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "SCBLMYKX",
                        "bank_name": "Standard Chartered Bank Malaysia Berhad",
                        "base_rate": 3.52,
                        "base_lending_rate": 6.7,
                        "indicative_eff_lending_rate": 4.52,
                    },
                    {
                        "bank_code": "UOVBMYKL",
                        "bank_name": "United Overseas Bank (Malaysia) Bhd.",
                        "base_rate": 3.86,
                        "base_lending_rate": 6.82,
                        "indicative_eff_lending_rate": 4.61,
                    },
                    {
                        "bank_code": "AIBBMYKL",
                        "bank_name": "Affin Islamic Bank Berhad",
                        "base_rate": 3.95,
                        "base_financing_rate": 6.81,
                        "indicative_eff_lending_rate": 4.76,
                    },
                    {
                        "bank_code": "ALSRMYKL",
                        "bank_name": "Alliance Islamic Bank Berhad",
                        "base_rate": 3.82,
                        "base_financing_rate": 6.67,
                        "indicative_eff_lending_rate": 4.36,
                    },
                    {
                        "bank_code": "AISLMYKL",
                        "bank_name": "AmBank Islamic Berhad",
                        "base_rate": 3.85,
                        "base_financing_rate": 6.7,
                        "indicative_eff_lending_rate": 4.5,
                    },
                    {
                        "bank_code": "BIMBMYKL",
                        "bank_name": "Bank Islam Malaysia Berhad",
                        "base_rate": 3.77,
                        "base_financing_rate": 6.72,
                        "indicative_eff_lending_rate": 4.57,
                    },
                    {
                        "bank_code": "BMMBMYKL",
                        "bank_name": "Bank Muamalat Malaysia Berhad",
                        "base_rate": 3.81,
                        "base_financing_rate": 6.81,
                        "indicative_eff_lending_rate": 4.81,
                    },
                    {
                        "bank_code": "CTBBMYKL",
                        "bank_name": "CIMB Islamic Bank Berhad",
                        "base_rate": 4,
                        "base_financing_rate": 6.85,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "HLIBMYKL",
                        "bank_name": "Hong Leong Islamic Bank Berhad",
                        "base_rate": 3.88,
                        "base_financing_rate": 6.89,
                        "indicative_eff_lending_rate": 4.6,
                    },
                    {
                        "bank_code": "HMABMYKL",
                        "bank_name": "HSBC Amanah Malaysia Berhad",
                        "base_rate": 3.64,
                        "base_financing_rate": 6.74,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "KFHOMYKL",
                        "bank_name": "Kuwait Finance House (Malaysia) Berhad",
                        "base_rate": 3.5,
                        "base_financing_rate": 7.39,
                        "indicative_eff_lending_rate": 4.45,
                    },
                    {
                        "bank_code": "MBISMYKL",
                        "bank_name": "Maybank Islamic Berhad",
                        "base_rate": 3,
                        "base_financing_rate": 6.65,
                        "indicative_eff_lending_rate": 4.35,
                    },
                    {
                        "bank_code": "AFBQMYKL",
                        "bank_name": "MBSB Bank Berhad",
                        "base_rate": 3.9,
                        "base_financing_rate": 6.75,
                        "indicative_eff_lending_rate": 4.45,
                    },
                    {
                        "bank_code": "OABBMYKL",
                        "bank_name": "OCBC Al-Amin Bank Berhad",
                        "base_rate": 3.83,
                        "base_financing_rate": 6.76,
                        "indicative_eff_lending_rate": 4.7,
                    },
                    {
                        "bank_code": "PUIBMYKL",
                        "bank_name": "Public Islamic Bank Berhad",
                        "base_rate": 3.52,
                        "base_financing_rate": 6.72,
                        "indicative_eff_lending_rate": 4.35,
                    },
                    {
                        "bank_code": "RHBAMYKL",
                        "bank_name": "RHB Islamic Bank Berhad",
                        "base_rate": 3.75,
                        "base_financing_rate": 6.7,
                        "indicative_eff_lending_rate": 4.75,
                    },
                    {
                        "bank_code": "SCSRMYKK",
                        "bank_name": "Standard Chartered Saadiq Berhad",
                        "base_rate": 3.52,
                        "base_financing_rate": 6.7,
                        "indicative_eff_lending_rate": 4.52,
                    },
                    {
                        "bank_code": "AGOBMYKL",
                        "bank_name": "Agrobank",
                        "base_rate": 3.6,
                        "base_financing_rate": 6.75,
                        "indicative_eff_lending_rate": null,
                    },
                    {
                        "bank_code": "BSNAMYK1",
                        "bank_name": "Bank Simpanan Nasional",
                        "base_rate": 3.85,
                        "base_financing_rate": 6.6,
                        "indicative_eff_lending_rate": 4.45,
                    },
                    {
                        "bank_code": "PHBMMYKL",
                        "bank_name": "Affin Bank Berhad",
                        "base_rate": 3.95,
                        "base_lending_rate": 6.81,
                        "indicative_eff_lending_rate": 4.76,
                    },
                    {
                        "bank_code": "MFBBMYKL",
                        "bank_name": "Alliance Bank Malaysia Berhad",
                        "base_rate": 3.82,
                        "base_lending_rate": 6.67,
                        "indicative_eff_lending_rate": 4.36,
                    },
                    {
                        "bank_code": "ARBKMYKL",
                        "bank_name": "AmBank (M) Berhad",
                        "base_rate": 3.85,
                        "base_lending_rate": 6.7,
                        "indicative_eff_lending_rate": 4.5,
                    },
                    {
                        "bank_code": "BKCHMYKL",
                        "bank_name": "Bank of China (M) Berhad",
                        "base_rate": 3.8,
                        "base_lending_rate": 6.6,
                        "indicative_eff_lending_rate": 4.8,
                    },
                    {
                        "bank_code": "RJHIMYKL",
                        "bank_name": "Al Rajhi Banking & Investment (M) Berhad",
                        "base_rate": 4.1,
                        "base_financing_rate": 7,
                        "indicative_eff_lending_rate": 5.45,
                    },
                    {
                        "bank_code": "BKRMMYKL",
                        "bank_name": "Bank Kerjasama Rakyat (M) Berhad",
                        "base_rate": 3.85,
                        "base_financing_rate": 6.83,
                        "indicative_eff_lending_rate": 4.65,
                    },
                ],
                "meta": {
                    "last_updated": "2019-05-23 15:45:40",
                    "total_result": 35,
                    "effective_date": "2019-06-14",
                },
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "base-rate/MBBEMYKL",
            json={
                "data": {
                    "bank_code": "MBBEMYKL",
                    "bank_name": "Malayan Banking Berhad",
                    "base_rate": 3,
                    "base_lending_rate": 6.65,
                    "indicative_eff_lending_rate": 4.35,
                },
                "meta": {
                    "effective_date": "2019-06-14",
                    "last_updated": "2019-05-23 15:18:34",
                    "total_result": 1,
                },
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "base-rate/CIBBMYKL",
            json={
                "data": {
                    "bank_code": "CIBBMYKL",
                    "bank_name": "CIMB Bank Berhad",
                    "base_rate": 4,
                    "base_lending_rate": 6.85,
                    "indicative_eff_lending_rate": 4.75,
                },
                "meta": {
                    "effective_date": "2019-06-14",
                    "last_updated": "2019-05-23 15:13:02",
                    "total_result": 1,
                },
            },
            status=200,
        )
        yield r


class TestBaseRate:
    def test_latest(self, mock_base_rate):
        br = Bnmpy().base_rate()
        assert br.endpoints == ["base-rate"]
        assert len(br.data) == 35
        assert all(
            [
                k in br.data[0]
                for k in [
                    "bank_code",
                    "bank_name",
                    "base_rate",
                    "base_lending_rate",
                    "indicative_eff_lending_rate",
                ]
            ]
        )

    def test_single(self, mock_base_rate):
        br = Bnmpy().base_rate("MBBEMYKL")
        assert br.endpoints == ["base-rate/MBBEMYKL"]
        assert len(br.data) == 1

    def test_multi(self, mock_base_rate):
        br = Bnmpy().base_rate(["MBBEMYKL", "CIBBMYKL"])
        assert br.endpoints == ["base-rate/MBBEMYKL", "base-rate/CIBBMYKL"]
        assert len(br.data) == 2
