from django.test import TestCase

"""
ユニットテストを素振りするためのクラス
"""
class TestSandbox(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        ・全テストで必要なリソース等を作成する
        ・データベースのクラスごとのトランザクション開始
        ・フィクスチャデータの生成
        ・cls.setUpTestData()が定義されていたら実行
        """
        # オーバーライドする場合は、最初に継承元のメソッドを呼ぶ
        super().setUpClass()
        # TODO: 事前処理

    @classmethod
    def setUpTestData(cls):
        """
        ・テストデータを生成する
        ・全テストメソッド終了後、テストデータは破棄（ロールバック）される
        """
    
    def setUp(self):
        """
        ・各テストメソッドの最初に実行される
        ・よく使う変数をselfに設定する等、テストクラスの最終準備
        """

    def tearDown(self):
        """
        ・各テストメソッドの最後に実行される
        ・setUp()に対する後始末処理などを定義する
        """

    @classmethod
    def tearDownClass(cls):
        """
        ・一時ファイルなど、setUpTestData()で破棄されないデータやファイルを削除する
        ・setUpClass()に対する後始末処理などを定義する
        """
        # オーバーライドする場合は、最初に継承元のメソッドを呼ぶ
        super().tearDownClass()
        # TODO: 事後処理

    def test_test(self):
        self.assertEqual(1,1)
