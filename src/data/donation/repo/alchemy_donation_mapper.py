from models.collect.donation_model import DonationModel
from src.dto.collects.collect import Collect
from src.dto.collects.donation import Donation
from src.dto.user.user import User


class DonationMapper:

    @staticmethod
    def to_dto(donation: DonationModel) -> Donation:
        author = User(**donation.author.dict()) if donation.author else None
        collect = Collect(**donation.collect.dict()) if donation.collect else None
        return Donation(
            collect=collect,
            author=author,
            amount=donation.amount,
            create_date=donation.create_date,
            status=donation.status,
            uid=donation.uid
        )

    @staticmethod
    def to_model(donation: Donation) -> DonationModel:
        author_uid = donation.author.uid if donation.author else None
        collect_uid = donation.collect.uid if donation.collect else None
        return DonationModel(
            uid=donation.uid,
            collect_id=collect_uid,
            author_id=author_uid,
            amount=donation.amount,
            create_date=donation.create_date,
            status=donation.status
        )
