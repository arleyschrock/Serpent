/// <summary>
/// Serpent, a Python literal expression serializer/deserializer
/// (a.k.a. Python's ast.literal_eval in .NET)
///
/// Copyright 2013, Irmen de Jong (irmen@razorvine.net)
/// This code is open-source, but licensed under the "MIT software license". See http://opensource.org/licenses/MIT
/// </summary>

using System;
using System.Text;

namespace Razorvine.Serpent
{

/// <summary>
/// A Complex Number class. 
/// </summary>
public struct ComplexNumber {
	
	public double Real;
	public double Imaginary;
	
	public ComplexNumber(double r, double i) {
		Real=r;
		Imaginary=i;
	}

	public override string ToString()
	{
		StringBuilder sb=new StringBuilder();
		sb.Append(Real);
		if(Imaginary>0)
			sb.Append('+');
		return sb.Append(Imaginary).Append('i').ToString();
	}

	public double Magnitude() {
		return Math.Sqrt(Real * Real + Imaginary * Imaginary);
	}

	public static ComplexNumber operator +(ComplexNumber c1, ComplexNumber c2) {
		return new ComplexNumber(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
	}


	public static ComplexNumber operator -(ComplexNumber c1, ComplexNumber c2) {
		return new ComplexNumber(c1.Real - c2.Real, c1.Imaginary - c2.Imaginary);
	}

	public static ComplexNumber operator *(ComplexNumber c1, ComplexNumber c2) {
		return new ComplexNumber(c1.Real * c2.Real - c1.Imaginary * c2.Imaginary, c1.Real * c2.Imaginary + c1.Imaginary * c2.Real);
	}

	public static ComplexNumber operator /(ComplexNumber c1, ComplexNumber c2) {
		return new ComplexNumber((c1.Real * c2.Real + c1.Imaginary * c2.Imaginary) / (c2.Real * c2.Real + c2.Imaginary * c2.Imaginary), (c1.Imaginary * c2.Real - c1.Real * c2.Imaginary)
				/ (c2.Real * c2.Real + c2.Imaginary * c2.Imaginary));
	}

	#region Equals and GetHashCode implementation
	public override bool Equals(object obj)
	{
		if(!(obj is ComplexNumber))
			return false;
		ComplexNumber other = (ComplexNumber) obj;
		return Real==other.Real && Imaginary==other.Imaginary;
	}
	
	public override int GetHashCode()
	{
		return (Real.GetHashCode()) ^ (Imaginary.GetHashCode());
	}
	
	public static bool operator ==(ComplexNumber lhs, ComplexNumber rhs)
	{
		if (ReferenceEquals(lhs, rhs))
			return true;
		if (ReferenceEquals(lhs, null) || ReferenceEquals(rhs, null))
			return false;
		return lhs.Equals(rhs);
	}
	
	public static bool operator !=(ComplexNumber lhs, ComplexNumber rhs)
	{
		return !(lhs == rhs);
	}
	#endregion
}

}