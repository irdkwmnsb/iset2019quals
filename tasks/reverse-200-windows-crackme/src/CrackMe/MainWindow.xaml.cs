using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.IO;
using Microsoft.Win32;
using System.Security;
using System.Numerics;

namespace CrackMe
{
    public partial class MainWindow : Window
    {
        byte[] notAFlag = new byte[] { 53, 41, 36, 37, 62, 47, 127, 57, 22, 165, 170, 210, 83, 193, 22, 208, 12, 137, 230, 79, 25, 242, 40, 12, 149, 23, 155, 238, 229, 243, 43, 95, 105, 142, 167, 112, 95, 54, 210, 247, 68, 112, 50, 98, 214, 236, 167, 121, 58, 124, 50};

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            CheckComputer();
            CheckLicenseKey();
        }

        private void CheckLicenseKey()
        {
            string encryptedData = "SAN";
            char[] secretData = new char[encryptedData.Length];
            secretData[2] = encryptedData[1];
            secretData[0] = encryptedData[2];
            secretData[1] = encryptedData[0];
            string notEncryptedData = "LOBEEEIVS";
            char[] notSecretData = new char[notEncryptedData.Length];
            notSecretData[1] = notEncryptedData[0];
            notSecretData[8] = notEncryptedData[8];
            notSecretData[2] = notEncryptedData[1];
            notSecretData[7] = notEncryptedData[3];
            notSecretData[0] = notEncryptedData[6];
            notSecretData[3] = notEncryptedData[7];
            notSecretData[5] = notEncryptedData[2];
            notSecretData[4] = notEncryptedData[3];
            notSecretData[6] = notEncryptedData[3];

            RegistryKey reg;
            try
            {
                reg = Registry.CurrentUser.OpenSubKey("SOFTWARE").OpenSubKey(new string(secretData));
            } catch(SecurityException)
            {
                InvalidLicense();
                return;
            } catch (ObjectDisposedException)
            {
                InvalidLicense();
                return;
            }
            if (reg == null)
            {
                InvalidLicense();
                return;
            }

            RegistryValueKind kind = reg.GetValueKind(new string(notSecretData));
            if (kind != RegistryValueKind.DWord)
            {
                InvalidLicense();
                return;
            }
            int value = (int)reg.GetValue(new string(notSecretData));
            if (value % 3571 != 0 && value % 2087 != 0 && value % 29 != 0)
            {
                InvalidLicense();
                return;
            }
			// g 956 m 13615801583 x 4296787130 a 2658442515
            BigInteger g = 956, m = 13615801583, a = 2658442515;
            long licenseKeyData;
            if (!long.TryParse(licenseKey.Text, out licenseKeyData))
            {
                InvalidLicense();
                return;
            }
            BigInteger x = new BigInteger(licenseKeyData);
            if (BigInteger.ModPow(g, x, m) != a)
            {
                InvalidLicense();
                return;
            }
            StartProgram(value, notSecretData, x.ToByteArray());
        }

        private void StartProgram(int value1, char[] value2, byte[] value3)
        {
            byte[] data = new byte[notAFlag.Length];
            byte[] value1Data = BitConverter.GetBytes(value1);
            for (int i = 0; i < value2.Length; ++i)
                data[i] = (byte)value2[value2.Length - i - 1];

            data[9] = value1Data[0];
            data[10] = value1Data[1];
            data[11] = value1Data[2];
            data[12] = value1Data[3];
            data[22] = 75;
            data[14] = 120;
            data[23] = 96;
            data[21] = 173;
            data[26] = 168;
            data[16] = 83;
            data[13] = 241;
            data[18] = 209;
            data[20] = 105;
            data[27] = 156;
            data[25] = 34;
            data[19] = 124;
            data[17] = 188;
            data[24] = 165;
            data[15] = 227;

            int currentPtr = 28;
            for (int i = 0; i < value3.Length; ++i)
                data[currentPtr++] = value3[i];
            for (int i = 0; i < value3.Length; ++i)
                data[currentPtr++] = value3[i];
            for (int i = 0; i < value3.Length; ++i)
                data[currentPtr++] = value3[i];

            data[43] = value1Data[3];
            data[44] = value1Data[2];
            data[45] = value1Data[1];
            data[46] = value1Data[0];

            data[47] = 73;
            data[48] = 84;
            data[49] = 77;
            data[50] = 79;

            char[] hmmmmm = new char[notAFlag.Length];

            for (int i = 0; i < hmmmmm.Length; ++i)
            {
                hmmmmm[i] = (char)(notAFlag[i] ^ data[i]);
            }

            panel.Visibility = Visibility.Hidden;
            flag.Text = new string(hmmmmm);
    }

        private void CheckComputer()
        {
            string encryptedData = "ca_mr_groepustprrsee";
            char[] secretData = new char[encryptedData.Length];

            secretData[5] = encryptedData[2];
            secretData[1] = encryptedData[11];
            secretData[17] = encryptedData[4];
            secretData[7] = encryptedData[9];
            secretData[2] = encryptedData[10];
            secretData[11] = encryptedData[13];
            secretData[14] = encryptedData[4];
            secretData[9] = encryptedData[4];
            secretData[8] = encryptedData[0];
            secretData[19] = encryptedData[3];
            secretData[15] = encryptedData[8];
            secretData[0] = encryptedData[12];
            secretData[6] = encryptedData[12];
            secretData[10] = encryptedData[9];
            secretData[16] = encryptedData[6];
            secretData[12] = encryptedData[2];
            secretData[4] = encryptedData[4];
            secretData[13] = encryptedData[10];
            secretData[3] = encryptedData[9];
            secretData[18] = encryptedData[1];

            if (new string(secretData) != new DirectoryInfo(Directory.GetCurrentDirectory()).Name)
            {
                SorryYourComputerIsNotSuitableForOurSoftwareSolution();
            }
        }

        private void SorryYourComputerIsNotSuitableForOurSoftwareSolution()
        {
            MessageBox.Show("Sorry, Your Computer Is Not Suitable For Our Software Solution", "Invalid configuration", MessageBoxButton.OK, MessageBoxImage.Error);
            Application.Current.Shutdown();
        }

        private void InvalidLicense()
        {
            MessageBox.Show("Are you h4ck3r? Your license is invalid!", "Invalid license", MessageBoxButton.OK, MessageBoxImage.Error);
            Application.Current.Shutdown();
        }
    }
}
