from datetime import datetime

import pytest
import responses

from main import BASE_URL, BaseRate, BnmpyItem, FxTurnOver


@pytest.fixture
def mock_basic():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as r:
        r.add(
            responses.GET, BASE_URL + "none", json={"data": None}, status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "single",
            json={"data": {"hello": "world"}},
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "list-single",
            json={"data": [{"hello": "world"}]},
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "list-multi",
            json={"data": [{"hello": "world"}, {"foo": "bar"}]},
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fail",
            json={"message": "No records found.", "code": 404},
            status=404,
        )
        yield r


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
                        "indicative_eff_lending_rate": None,
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


@pytest.fixture
def mock_fx_turn_over():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as r:
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over",
            json={
                "data": {"date": "2019-11-04", "total_sum": 10.08},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/date/2019-01-02",
            json={
                "data": {"date": "2019-01-02", "total_sum": 11.7},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/date/2019-01-03",
            json={
                "data": {"date": "2019-01-03", "total_sum": 12.93},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/date/2019-01-04",
            json={
                "data": {"date": "2019-01-04", "total_sum": 12.88},
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 1},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/year/2019/month/01",
            json={
                "data": [
                    {"date": "2019-01-31", "total_sum": 14.17},
                    {"date": "2019-01-30", "total_sum": 11.7},
                    {"date": "2019-01-29", "total_sum": 12.68},
                    {"date": "2019-01-28", "total_sum": 10.4},
                    {"date": "2019-01-25", "total_sum": 15.23},
                    {"date": "2019-01-24", "total_sum": 13.67},
                    {"date": "2019-01-23", "total_sum": 13.73},
                    {"date": "2019-01-22", "total_sum": 16.57},
                    {"date": "2019-01-18", "total_sum": 12.84},
                    {"date": "2019-01-17", "total_sum": 14.26},
                    {"date": "2019-01-16", "total_sum": 12.57},
                    {"date": "2019-01-15", "total_sum": 12.18},
                    {"date": "2019-01-14", "total_sum": 13.75},
                    {"date": "2019-01-11", "total_sum": 12.46},
                    {"date": "2019-01-10", "total_sum": 13.02},
                    {"date": "2019-01-09", "total_sum": 13.49},
                    {"date": "2019-01-08", "total_sum": 11.45},
                    {"date": "2019-01-07", "total_sum": 14.28},
                    {"date": "2019-01-04", "total_sum": 12.88},
                    {"date": "2019-01-03", "total_sum": 12.93},
                    {"date": "2019-01-02", "total_sum": 11.7},
                ],
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 21},
            },
            status=200,
        )
        r.add(
            responses.GET,
            BASE_URL + "fx-turn-over/year/2019/month/02",
            json={
                "data": [
                    {"date": "2019-02-28", "total_sum": 12.84},
                    {"date": "2019-02-27", "total_sum": 13.71},
                    {"date": "2019-02-26", "total_sum": 13.39},
                    {"date": "2019-02-25", "total_sum": 11.21},
                    {"date": "2019-02-22", "total_sum": 12.87},
                    {"date": "2019-02-21", "total_sum": 13.05},
                    {"date": "2019-02-20", "total_sum": 13.55},
                    {"date": "2019-02-19", "total_sum": 11.54},
                    {"date": "2019-02-18", "total_sum": 6.01},
                    {"date": "2019-02-15", "total_sum": 10.25},
                    {"date": "2019-02-14", "total_sum": 12.83},
                    {"date": "2019-02-13", "total_sum": 11.71},
                    {"date": "2019-02-12", "total_sum": 12.87},
                    {"date": "2019-02-11", "total_sum": 11.68},
                    {"date": "2019-02-08", "total_sum": 10.79},
                    {"date": "2019-02-07", "total_sum": 11.37},
                    {"date": "2019-02-04", "total_sum": 10.69},
                ],
                "meta": {"last_updated": "2019-11-04 07:00:06", "total_result": 17},
            },
            status=200,
        )
        yield r


@pytest.fixture
def mock_boilerplate():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as r:
        r.add(
            responses.GET, BASE_URL + "sample", json={}, status=200,
        )
        r.add(
            responses.GET, BASE_URL + "sample", json={}, status=200,
        )
        r.add(
            responses.GET, BASE_URL + "sample", json={}, status=200,
        )
        r.add(
            responses.GET, BASE_URL + "sample", json={}, status=200,
        )
        yield r


class TestBnmpyItem:
    def test_data_single(self, mock_basic):
        b = BnmpyItem("single")
        assert b.data == [{"hello": "world"}]

    def test_data_list_single(self, mock_basic):
        b = BnmpyItem("list-single")
        assert b.data == [{"hello": "world"}]

    def test_data_list_multi(self, mock_basic):
        b = BnmpyItem("list-multi")
        assert b.data == [{"hello": "world"}, {"foo": "bar"}]

    def test_data_none(self, mock_basic):
        b = BnmpyItem("none")
        assert b.data == []

    def test_data_list_combine(self, mock_basic):
        b = BnmpyItem(["none", "single", "list-single", "list-multi", "fail"])
        assert b.data == [
            {"hello": "world"},
            {"hello": "world"},
            {"hello": "world"},
            {"foo": "bar"},
        ]


class TestBaseRate:
    def test_latest(self, mock_base_rate):
        br = BaseRate()
        assert br.endpoints == ["base-rate"]
        assert len(br.data) == 35
        assert all(
            [
                k in br.data[0].keys()
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
        br = BaseRate("MBBEMYKL")
        assert br.endpoints == ["base-rate/MBBEMYKL"]
        assert len(br.data) == 1

    def test_multi(self, mock_base_rate):
        br = BaseRate(["MBBEMYKL", "CIBBMYKL"])
        assert br.endpoints == ["base-rate/MBBEMYKL", "base-rate/CIBBMYKL"]
        assert len(br.data) == 2


class TestFxTurnOver:
    def test_latest(self, mock_fx_turn_over):
        fto = FxTurnOver()
        assert fto.endpoints == ["fx-turn-over"]
        assert len(fto.data) == 1
        assert all([k in fto.data[0].keys() for k in ["date", "total_sum"]])

    def test_date_single(self, mock_fx_turn_over):
        fto = FxTurnOver(dates=datetime(2019, 1, 2))
        assert fto.endpoints == ["fx-turn-over/date/2019-01-02"]
        assert len(fto.data) == 1

    def test_date_multi(self, mock_fx_turn_over):
        fto = FxTurnOver(dates=[datetime(2019, 1, 2), datetime(2019, 1, 3)])
        assert fto.endpoints == [
            "fx-turn-over/date/2019-01-02",
            "fx-turn-over/date/2019-01-03",
        ]
        assert len(fto.data) == 2

    def test_range_within_month(self, mock_fx_turn_over):
        fto = FxTurnOver(start=datetime(2019, 1, 2), end=datetime(2019, 1, 4))
        assert fto.endpoints == ["fx-turn-over/year/2019/month/01"]
        assert len(fto.data) == 3

    def test_range_across_months(self, mock_fx_turn_over):
        fto = FxTurnOver(start=datetime(2019, 1, 29), end=datetime(2019, 2, 4))
        assert fto.endpoints == [
            "fx-turn-over/year/2019/month/01",
            "fx-turn-over/year/2019/month/02",
        ]
        assert len(fto.data) == 4
